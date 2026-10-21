"""Shared, environment-configured model construction."""

import os
from functools import lru_cache

from langchain_openai import ChatOpenAI


def _required_api_key() -> str:
    api_key = os.environ.get("API_KEY")
    if not api_key:
        raise RuntimeError(
            "API_KEY is not set. Configure a rotated API key in the "
            "environment before running the network."
        )
    return api_key


@lru_cache(maxsize=3)
def get_model(role: str) -> ChatOpenAI:
    """Construct one of the three independently configurable model clients."""
    model_variables = {
        "extract": ("EXTRACTION_MODEL", "gpt-6-luna", 180),
        "normalize": ("NORMALIZATION_MODEL", "gpt-5.4-nano", 300),
        "review": ("REVIEW_MODEL", "gpt-5.6-luna", 180),
    }
    try:
        env_name, default_model, default_timeout = model_variables[role]
    except KeyError as exc:
        raise ValueError(f"Unknown model role: {role}") from exc

    timeout = os.environ.get(
        f"{role.upper()}_TIMEOUT_SECONDS",
        os.environ.get("OPENAI_TIMEOUT_SECONDS", str(default_timeout)),
    )
    options: dict[str, object] = {
        "model": os.environ.get(env_name, default_model),
        "api_key": _required_api_key(),
        "timeout": float(timeout),
        "max_retries": int(os.environ.get("OPENAI_MAX_RETRIES", "2")),
    }
    base_url = os.environ.get("OPENAI_BASE_URL")
    if base_url:
        options["base_url"] = base_url
    return ChatOpenAI(**options)
