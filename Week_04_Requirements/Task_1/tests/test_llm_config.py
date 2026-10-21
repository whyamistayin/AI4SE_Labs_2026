import os
import unittest
from unittest.mock import patch

from requirements_network import llm


class ModelConfigurationTests(unittest.TestCase):
    def tearDown(self):
        llm.get_model.cache_clear()

    def test_normalization_timeout_can_be_configured_independently(self):
        llm.get_model.cache_clear()
        with (
            patch.dict(
                os.environ,
                {"API_KEY": "test-key", "NORMALIZE_TIMEOUT_SECONDS": "42"},
                clear=True,
            ),
            patch("requirements_network.llm.ChatOpenAI") as chat_model,
        ):
            llm.get_model("normalize")

        self.assertEqual(chat_model.call_args.kwargs["timeout"], 42.0)
        self.assertEqual(chat_model.call_args.kwargs["model"], "gpt-5.4-nano")

    def test_role_defaults_use_the_selected_models(self):
        for role, expected_model in (
            ("extract", "gpt-6-luna"),
            ("normalize", "gpt-5.4-nano"),
            ("review", "gpt-5.6-luna"),
        ):
            with self.subTest(role=role):
                llm.get_model.cache_clear()
                with (
                    patch.dict(os.environ, {"API_KEY": "test-key"}, clear=True),
                    patch("requirements_network.llm.ChatOpenAI") as chat_model,
                ):
                    llm.get_model(role)
                self.assertEqual(
                    chat_model.call_args.kwargs["model"], expected_model
                )

    def test_global_timeout_overrides_role_default(self):
        llm.get_model.cache_clear()
        with (
            patch.dict(
                os.environ,
                {"API_KEY": "test-key", "OPENAI_TIMEOUT_SECONDS": "55"},
                clear=True,
            ),
            patch("requirements_network.llm.ChatOpenAI") as chat_model,
        ):
            llm.get_model("normalize")

        self.assertEqual(chat_model.call_args.kwargs["timeout"], 55.0)

    def test_missing_api_key_fails_explicitly(self):
        llm.get_model.cache_clear()
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(RuntimeError, "API_KEY is not set"):
                llm.get_model("normalize")


if __name__ == "__main__":
    unittest.main()
