import unittest
from unittest.mock import Mock, patch

from pydantic import ValidationError

from requirements_network.normalization_node import (
    _normalization_schema,
    normalize_requirements,
)
from requirements_network.schemas import (
    NormalizationResult,
    Requirement,
    SourceReference,
)


def make_result(candidate_id: str) -> NormalizationResult:
    return NormalizationResult(
        requirements=[
            Requirement(
                name="Report export",
                description="Staff can export reports.",
                priority="Should",
                sources=[SourceReference(candidate_id=candidate_id)],
            )
        ],
        discarded=[],
    )


def make_state() -> dict:
    return {
        "documents": [{"document_id": "DOC-test", "path": "source.txt"}],
        "candidates": [
            {
                "candidate_id": "DOC-test-C001-R001",
                "name": "Export",
                "description": "Staff can export reports.",
                "priority": "Should",
                "evidence": "export reports",
                "document_id": "DOC-test",
                "path": "source.txt",
                "chunk_id": "DOC-test-C001",
                "start_line": 1,
                "end_line": 1,
            }
        ],
        "review_findings": [],
        "revision_round": 0,
    }


class NormalizationCitationTests(unittest.TestCase):
    def test_schema_restricts_citations_to_extracted_candidate_ids(self):
        schema = _normalization_schema({"DOC-test-C001-R001"})

        valid = make_result("DOC-test-C001-R001")
        invalid = make_result("DOC-test-C001-R019")
        self.assertEqual(
            schema.model_validate(valid.model_dump())
            .requirements[0]
            .sources[0]
            .candidate_id,
            "DOC-test-C001-R001",
        )
        with self.assertRaises(ValidationError):
            schema.model_validate(invalid.model_dump())

    def test_uses_constrained_schema_for_normalization_response(self):
        model = Mock()
        model.with_structured_output.return_value = model
        model.invoke.return_value = make_result("DOC-test-C001-R001")

        with patch("requirements_network.normalization_node.get_model", return_value=model):
            result = normalize_requirements(make_state())

        self.assertEqual(model.invoke.call_count, 1)
        schema = model.with_structured_output.call_args.args[0]
        with self.assertRaises(ValidationError):
            schema.model_validate(make_result("DOC-test-C001-R019").model_dump())
        self.assertEqual(
            result["requirements"][0].sources[0].candidate_id,
            "DOC-test-C001-R001",
        )

    def test_empty_candidate_set_skips_normalization_call(self):
        model = Mock()
        state = make_state()
        state["candidates"] = []

        with patch("requirements_network.normalization_node.get_model", return_value=model):
            result = normalize_requirements(state)

        self.assertEqual(model.invoke.call_count, 0)
        self.assertEqual(result["requirements"], [])
        self.assertEqual(result["discarded"], [])


class FeedbackRouteTests(unittest.TestCase):
    def test_extraction_issue_skips_unproductive_normalization_feedback(self):
        from requirements_network.workflow import _review_route

        self.assertEqual(
            _review_route(
                {
                    "extraction_issues": [
                        {
                            "path": "source.txt",
                            "chunk_id": "DOC-test-C001",
                            "start_line": 1,
                            "end_line": 2,
                            "unverified_candidate_count": 1,
                        }
                    ],
                    "review_findings": [],
                    "revision_round": 0,
                    "max_revision_rounds": 2,
                }
            ),
            "finish",
        )


if __name__ == "__main__":
    unittest.main()
