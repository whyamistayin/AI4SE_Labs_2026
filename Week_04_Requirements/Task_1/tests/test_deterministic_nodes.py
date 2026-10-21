import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from requirements_network.extraction_node import extract_candidates
from requirements_network.finalization_node import finalize_output
from requirements_network.ingestion_node import _chunk_document, ingest_documents
from requirements_network.schemas import (
    CandidateRequirement,
    ExtractionResult,
    Requirement,
    SourceReference,
)
from requirements_network.text_utils import find_source_excerpt


class EvidenceTests(unittest.TestCase):
    def test_matches_word_sequence_despite_punctuation_and_whitespace(self):
        source = 'The system shall export reports, including staff reports.'

        excerpt = find_source_excerpt(source, '"system shall export reports including"')

        self.assertEqual(excerpt, "system shall export reports, including")

    def test_rejects_paraphrased_or_noncontiguous_evidence(self):
        source = "The system shall export reports for staff."

        self.assertIsNone(find_source_excerpt(source, "The system must export reports"))
        self.assertIsNone(find_source_excerpt(source, "The system export reports"))

    def test_extraction_assigns_candidate_id_and_canonical_source_quote(self):
        model_result = ExtractionResult(
            requirements=[
                CandidateRequirement(
                    name="Report export",
                    description="The system should export reports.",
                    priority="Should",
                    evidence='"system shall export reports including"',
                )
            ]
        )
        model = Mock()
        model.with_structured_output.return_value = model
        model.invoke.return_value = model_result
        state = {
            "chunks": [
                {
                    "chunk_id": "DOC-test-C001",
                    "document_id": "DOC-test",
                    "path": "source.txt",
                    "start_line": 1,
                    "end_line": 1,
                    "text": "The system shall export reports, including summaries.",
                }
            ]
        }

        with patch("requirements_network.extraction_node.get_model", return_value=model):
            result = extract_candidates(state)

        self.assertEqual(
            result["candidates"][0]["candidate_id"], "DOC-test-C001-R001"
        )
        self.assertEqual(
            result["candidates"][0]["evidence"],
            "system shall export reports, including",
        )

    def test_unverifiable_candidate_is_reported_without_aborting_chunk(self):
        first_result = ExtractionResult(
            requirements=[
                CandidateRequirement(
                    name="Unverified requirement",
                    description="Invented evidence.",
                    priority="Should",
                    evidence="A phrase not in the source.",
                ),
                CandidateRequirement(
                    name="Report export",
                    description="The system exports reports.",
                    priority="Must",
                    evidence="The system shall export reports.",
                ),
            ]
        )
        retry_result = ExtractionResult(
            requirements=[
                CandidateRequirement(
                    name="Still unverified",
                    description="Unverified candidate.",
                    priority="Should",
                    evidence="Still not present in the source.",
                ),
                CandidateRequirement(
                    name="Report export",
                    description="The system exports reports.",
                    priority="Must",
                    evidence="The system shall export reports.",
                ),
            ]
        )
        model = Mock()
        model.with_structured_output.return_value = model
        model.invoke.side_effect = [first_result, retry_result]
        state = {
            "chunks": [
                {
                    "chunk_id": "DOC-test-C001",
                    "document_id": "DOC-test",
                    "path": "source.txt",
                    "start_line": 1,
                    "end_line": 1,
                    "text": "The system shall export reports.",
                }
            ]
        }

        with patch("requirements_network.extraction_node.get_model", return_value=model):
            result = extract_candidates(state)

        self.assertEqual(model.invoke.call_count, 2)
        self.assertEqual(len(result["candidates"]), 1)
        self.assertEqual(result["candidates"][0]["name"], "Report export")
        self.assertEqual(
            result["extraction_issues"],
            [
                {
                    "path": "source.txt",
                    "chunk_id": "DOC-test-C001",
                    "start_line": 1,
                    "end_line": 1,
                    "unverified_candidate_count": 1,
                }
            ],
        )

    def test_empty_retry_does_not_silently_erase_initial_valid_candidates(self):
        first_result = ExtractionResult(
            requirements=[
                CandidateRequirement(
                    name="Unverified requirement",
                    description="Unverified initial evidence.",
                    priority="Should",
                    evidence="Not a source quotation.",
                ),
                CandidateRequirement(
                    name="Verified requirement",
                    description="The system shall export reports.",
                    priority="Must",
                    evidence="The system shall export reports.",
                ),
            ]
        )
        model = Mock()
        model.with_structured_output.return_value = model
        model.invoke.side_effect = [first_result, ExtractionResult(requirements=[])]
        state = {
            "chunks": [
                {
                    "chunk_id": "DOC-test-C001",
                    "document_id": "DOC-test",
                    "path": "source.txt",
                    "start_line": 1,
                    "end_line": 1,
                    "text": "The system shall export reports.",
                }
            ]
        }

        with patch("requirements_network.extraction_node.get_model", return_value=model):
            result = extract_candidates(state)

        self.assertEqual(len(result["candidates"]), 1)
        self.assertEqual(
            result["candidates"][0]["name"], "Verified requirement"
        )
        self.assertEqual(
            result["extraction_issues"][0]["unverified_candidate_count"], 1
        )


class IngestionTests(unittest.TestCase):
    def test_discovers_nested_text_and_email_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "nested").mkdir()
            (root / "nested" / "source.txt").write_text("A requirement.\n")
            (root / "mail.eml").write_text(
                "From: analyst@example.org\n"
                "Subject: Feature\n"
                "Content-Type: text/plain; charset=utf-8\n\n"
                "The system shall export reports.\n"
            )
            (root / "ignored.md").write_text("Not supported.")

            result = ingest_documents({"input_dir": str(root)})

        self.assertEqual(
            {document["path"] for document in result["documents"]},
            {"nested/source.txt", "mail.eml"},
        )
        mail = next(doc for doc in result["documents"] if doc["path"] == "mail.eml")
        self.assertIn("The system shall export reports.", mail["text"])

    def test_chunks_have_bounded_size_and_overlapping_lines(self):
        document = {
            "document_id": "DOC-test",
            "path": "source.txt",
            "text": "\n".join(f"line {index}" for index in range(1, 12)),
        }
        chunks = _chunk_document(document, chunk_chars=25, overlap_chars=10)

        self.assertGreater(len(chunks), 1)
        self.assertTrue(
            all(chunk["start_line"] <= chunk["end_line"] for chunk in chunks)
        )
        self.assertTrue(
            any(
                left["end_line"] >= right["start_line"]
                for left, right in zip(chunks, chunks[1:])
            )
        )

    def test_splits_a_single_very_long_line(self):
        document = {
            "document_id": "DOC-long",
            "path": "source.txt",
            "text": "x" * 100,
        }

        chunks = _chunk_document(document, chunk_chars=20, overlap_chars=5)

        self.assertGreater(len(chunks), 1)
        self.assertTrue(all(len(chunk["text"]) <= 20 for chunk in chunks))
        self.assertTrue(all(chunk["start_line"] == chunk["end_line"] == 1 for chunk in chunks))


class FinalizationTests(unittest.TestCase):
    def test_writes_unique_id_priority_and_traceable_requirement(self):
        requirement = Requirement(
            name="Report export",
            description="The system shall allow staff to export reports.",
            priority="Must",
            sources=[
                SourceReference(
                    candidate_id="DOC-test-C001-R001",
                )
            ],
        )
        state = {
            "output_path": "requirements.md",
            "documents": [
                {
                    "document_id": "DOC-test",
                    "path": "source.txt",
                    "text": "The system shall allow staff to export reports.\nOther line.",
                }
            ],
            "chunks": [
                {
                    "chunk_id": "DOC-test-C001",
                    "document_id": "DOC-test",
                    "path": "source.txt",
                    "start_line": 1,
                    "end_line": 2,
                    "text": "The system shall allow staff to export reports.\nOther line.",
                }
            ],
            "candidates": [
                {
                    "candidate_id": "DOC-test-C001-R001",
                    "name": "Report export",
                    "description": requirement.description,
                    "priority": "Must",
                    "evidence": "allow staff to export",
                    "document_id": "DOC-test",
                    "path": "source.txt",
                    "chunk_id": "DOC-test-C001",
                    "start_line": 1,
                    "end_line": 2,
                }
            ],
            "requirements": [requirement],
            "discarded": [],
            "review_findings": [],
            "review_approved": True,
            "revision_round": 0,
        }
        with tempfile.TemporaryDirectory() as directory:
            state["output_path"] = str(Path(directory) / "requirements.md")
            result = finalize_output(state)
            markdown = Path(result["output_path"]).read_text()

        self.assertIn("REQ-001: Report export", markdown)
        self.assertIn("**Priority:** Must", markdown)
        self.assertIn("`source.txt` (lines 1-2", markdown)
        self.assertIn("## Discarded or conflicting candidates", markdown)
        self.assertIn("## Extraction gaps", markdown)
        self.assertIn("_No extraction evidence gaps were reported._", markdown)

    def test_rejects_model_generated_unverified_source_evidence(self):
        requirement = Requirement(
            name="Export",
            description="The system exports reports.",
            priority="Should",
            sources=[
                SourceReference(
                    candidate_id="DOC-test-C001-R999",
                )
            ],
        )
        state = {
            "output_path": "requirements.md",
            "documents": [{"document_id": "DOC-test", "path": "source.txt"}],
            "chunks": [
                {
                    "chunk_id": "DOC-test-C001",
                    "document_id": "DOC-test",
                    "path": "source.txt",
                    "start_line": 1,
                    "end_line": 1,
                    "text": "The system shall export reports.",
                }
            ],
            "candidates": [
                {
                    "candidate_id": "DOC-test-C001-R001",
                    "name": "Export",
                    "description": "The system exports reports.",
                    "priority": "Should",
                    "evidence": "The system shall export",
                    "document_id": "DOC-test",
                    "path": "source.txt",
                    "chunk_id": "DOC-test-C001",
                    "start_line": 1,
                    "end_line": 1,
                }
            ],
            "requirements": [requirement],
            "discarded": [],
            "review_findings": [],
        }

        with self.assertRaisesRegex(ValueError, "Unknown extracted candidate"):
            finalize_output(state)

    def test_uses_extractor_quote_not_normalizer_rewritten_quote(self):
        requirement = Requirement(
            name="Report scheduling",
            description="The system shall schedule reports.",
            priority="Should",
            sources=[SourceReference(candidate_id="DOC-test-C001-R001")],
        )
        state = {
            "output_path": "requirements.md",
            "documents": [{"document_id": "DOC-test", "path": "source.txt"}],
            "chunks": [
                {
                    "chunk_id": "DOC-test-C001",
                    "document_id": "DOC-test",
                    "path": "source.txt",
                    "start_line": 1,
                    "end_line": 1,
                    "text": "Staff can schedule reports weekly.",
                }
            ],
            "candidates": [
                {
                    "candidate_id": "DOC-test-C001-R001",
                    "name": "Scheduling",
                    "description": "Staff can schedule reports.",
                    "priority": "Should",
                    "evidence": "schedule reports weekly",
                    "document_id": "DOC-test",
                    "path": "source.txt",
                    "chunk_id": "DOC-test-C001",
                    "start_line": 1,
                    "end_line": 1,
                }
            ],
            "requirements": [requirement],
            "discarded": [],
            "review_findings": [],
            "review_approved": True,
            "revision_round": 0,
        }

        with tempfile.TemporaryDirectory() as directory:
            state["output_path"] = str(Path(directory) / "requirements.md")
            result = finalize_output(state)
            markdown = Path(result["output_path"]).read_text()

        self.assertIn("> schedule reports weekly", markdown)


if __name__ == "__main__":
    unittest.main()
