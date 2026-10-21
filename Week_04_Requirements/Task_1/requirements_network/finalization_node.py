"""Deterministic validation and Markdown rendering of the final result."""

from pathlib import Path
import re

from .schemas import Requirement, SourceReference
from .state import CandidateRecord, NetworkState
from .text_utils import find_source_excerpt


def _unique_requirements(requirements: list[Requirement]) -> list[Requirement]:
    seen: set[tuple[str, str]] = set()
    unique = []
    for requirement in sorted(
        requirements, key=lambda item: (item.name.casefold(), item.description.casefold())
    ):
        key = (
            re.sub(r"\W+", " ", requirement.name.casefold()).strip(),
            re.sub(r"\W+", " ", requirement.description.casefold()).strip(),
        )
        if key in seen:
            raise ValueError(
                "Duplicate requirement remained after review: "
                f"{requirement.name!r}. Refusing to emit ambiguous output."
            )
        seen.add(key)
        unique.append(requirement)
    return unique


def _source_candidate(
    state: NetworkState, source: SourceReference
) -> CandidateRecord:
    candidate = next(
        (
            candidate
            for candidate in state["candidates"]
            if candidate["candidate_id"] == source.candidate_id
        ),
        None,
    )
    if candidate is None:
        raise ValueError(
            f"Unknown extracted candidate in requirement provenance: "
            f"{source.candidate_id}"
        )
    chunk = next(
        (
            chunk
            for chunk in state["chunks"]
            if chunk["chunk_id"] == candidate["chunk_id"]
        ),
        None,
    )
    if (
        chunk is None
        or chunk["document_id"] != candidate["document_id"]
        or chunk["path"] != candidate["path"]
        or chunk["start_line"] != candidate["start_line"]
        or chunk["end_line"] != candidate["end_line"]
    ):
        raise ValueError(
            f"Extracted candidate has invalid source metadata: "
            f"{candidate['candidate_id']}"
        )
    excerpt = find_source_excerpt(chunk["text"], candidate["evidence"])
    if excerpt != candidate["evidence"]:
        raise ValueError(
            f"Extracted candidate evidence is not verbatim source text: "
            f"{candidate['candidate_id']}"
        )
    return candidate


def _validate_references(state: NetworkState) -> None:
    known_documents = {
        document["document_id"]: document["path"] for document in state["documents"]
    }
    candidate_ids = [candidate["candidate_id"] for candidate in state["candidates"]]
    if len(candidate_ids) != len(set(candidate_ids)):
        raise ValueError("Extracted candidate IDs are not unique.")
    for item in [*state["requirements"], *state["discarded"]]:
        if not item.sources:
            raise ValueError(f"Requirement has no provenance: {item.name}")
        for source in item.sources:
            candidate = _source_candidate(state, source)
            if known_documents.get(candidate["document_id"]) != candidate["path"]:
                raise ValueError(
                    f"Invalid source document for candidate "
                    f"{candidate['candidate_id']} in requirement {item.name!r}"
                )


def _markdown(state: NetworkState) -> str:
    requirements = _unique_requirements(state["requirements"])
    _validate_references(state)
    lines = [
        "# Software Requirements Specification",
        "",
        f"Generated from {len(state['documents'])} source documents.",
        "",
        "## Priority scale",
        "",
        "- **Must** — Essential or explicitly mandatory for the system.",
        "- **Should** — Important, but a viable workaround exists.",
        "- **Could** — Desirable or explicitly optional.",
        "",
        "## Requirements",
        "",
    ]
    if not requirements:
        lines.append("_No software requirements were identified._")
        lines.append("")
    for index, requirement in enumerate(requirements, start=1):
        lines.extend(
            [
                f"### REQ-{index:03d}: {requirement.name}",
                "",
                f"**Priority:** {requirement.priority}",
                "",
                requirement.description,
                "",
                "**Derived from:**",
            ]
        )
        for source in requirement.sources:
            candidate = _source_candidate(state, source)
            lines.append(
                f"- `{candidate['path']}` "
                f"(lines {candidate['start_line']}-{candidate['end_line']}; "
                f"{candidate['document_id']}, {candidate['chunk_id']}, "
                f"{candidate['candidate_id']}) - "
                f"> {candidate['evidence'].replace(chr(10), ' ')}"
            )
        lines.append("")

    lines.extend(["## Discarded or conflicting candidates", ""])
    if not state["discarded"]:
        lines.extend(["_No candidates were discarded._", ""])
    for item in state["discarded"]:
        lines.extend(
            [
                f"### {item.name}",
                "",
                item.description,
                "",
                f"**Disposition:** {item.reason}",
                "",
                "**Derived from:**",
            ]
        )
        for source in item.sources:
            candidate = _source_candidate(state, source)
            lines.append(
                f"- `{candidate['path']}` "
                f"(lines {candidate['start_line']}-{candidate['end_line']}; "
                f"{candidate['document_id']}, {candidate['chunk_id']}, "
                f"{candidate['candidate_id']}) - "
                f"> {candidate['evidence'].replace(chr(10), ' ')}"
            )
        lines.append("")

    lines.extend(["## Extraction gaps", ""])
    extraction_issues = state.get("extraction_issues", [])
    if not extraction_issues:
        lines.extend(["_No extraction evidence gaps were reported._", ""])
    else:
        lines.extend(
            [
                "Some model-produced candidates were excluded because their "
                "evidence could not be verified against the source. Requirements "
                "from these ranges may be incomplete; inspect them before treating "
                "this document as complete.",
                "",
            ]
        )
        for issue in extraction_issues:
            lines.append(
                f"- `{issue['path']}` (lines {issue['start_line']}-"
                f"{issue['end_line']}; {issue['chunk_id']}): "
                f"{issue['unverified_candidate_count']} candidate(s) excluded "
                "after evidence verification failed."
            )
        lines.append("")

    lines.extend(["## Review status", ""])
    if state.get("review_approved"):
        lines.append("Approved by the independent quality-review node.")
    else:
        lines.append(
            "Not fully approved; the bounded review loop ended with findings. "
            "Unresolved findings are recorded below."
        )
    lines.append("")
    findings = state.get("review_findings", [])
    if findings:
        lines.extend(["### Unresolved findings", ""])
        for finding in findings:
            affected = (
                ", ".join(finding.affected_requirement_names)
                if finding.affected_requirement_names
                else "Corpus-wide"
            )
            lines.extend(
                [
                    f"- **{finding.severity.title()} - {affected}:** "
                    f"{finding.explanation} "
                    f"**Recommended action:** {finding.recommended_action}",
                ]
            )
        lines.append("")
    return "\n".join(lines)


def finalize_output(state: NetworkState) -> dict:
    output_path = Path(state["output_path"]).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    markdown = _markdown(state)
    output_path.write_text(markdown, encoding="utf-8")
    return {"output_path": str(output_path)}
