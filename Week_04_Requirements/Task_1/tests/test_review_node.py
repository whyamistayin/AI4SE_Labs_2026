import unittest
from unittest.mock import Mock, patch

from requirements_network.review_node import review_requirements
from requirements_network.schemas import ReviewResult


class ReviewExtractionIssueTests(unittest.TestCase):
    def test_extraction_gap_prevents_review_approval_and_is_reported(self):
        model = Mock()
        model.with_structured_output.return_value = model
        model.invoke.return_value = ReviewResult(approved=True, findings=[])
        state = {
            "documents": [{"document_id": "DOC-test", "path": "source.txt"}],
            "candidates": [],
            "extraction_issues": [
                {
                    "path": "source.txt",
                    "chunk_id": "DOC-test-C001",
                    "start_line": 4,
                    "end_line": 9,
                    "unverified_candidate_count": 2,
                }
            ],
            "requirements": [],
            "discarded": [],
        }

        with patch("requirements_network.review_node.get_model", return_value=model):
            result = review_requirements(state)

        self.assertFalse(result["review_approved"])
        self.assertEqual(len(result["review_findings"]), 1)
        self.assertEqual(result["review_findings"][0].severity, "high")
        self.assertIn("source.txt", result["review_findings"][0].explanation)


if __name__ == "__main__":
    unittest.main()
