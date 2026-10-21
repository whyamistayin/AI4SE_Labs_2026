"""Text normalization helpers used only for evidence integrity checks."""

import re


def _tokens_with_spans(value: str) -> list[tuple[str, int, int]]:
    return [
        (match.group().casefold(), match.start(), match.end())
        for match in re.finditer(r"\w+", value, flags=re.UNICODE)
    ]


def find_source_excerpt(source: str, evidence: str) -> str | None:
    """Return source text containing the same contiguous words as the evidence.

    Word sequence must match exactly; punctuation, quotes, and whitespace may
    differ due to model formatting. Returning the source slice preserves the
    original wording and punctuation for downstream traceability.
    """
    source_tokens = _tokens_with_spans(source)
    evidence_tokens = [token for token, _, _ in _tokens_with_spans(evidence)]
    if not evidence_tokens or len(evidence_tokens) > len(source_tokens):
        return None

    width = len(evidence_tokens)
    for start in range(len(source_tokens) - width + 1):
        window = source_tokens[start : start + width]
        if [token for token, _, _ in window] == evidence_tokens:
            return source[window[0][1] : window[-1][2]]
    return None
