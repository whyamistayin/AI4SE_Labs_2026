"""Typed state passed between LangGraph nodes."""

from typing import TypedDict

from .schemas import (
    DiscardedCandidate,
    Requirement,
    ReviewFinding,
)


class SourceDocument(TypedDict):
    document_id: str
    path: str
    text: str


class DocumentChunk(TypedDict):
    chunk_id: str
    document_id: str
    path: str
    start_line: int
    end_line: int
    text: str


class CandidateRecord(TypedDict):
    candidate_id: str
    name: str
    description: str
    priority: str
    evidence: str
    document_id: str
    path: str
    chunk_id: str
    start_line: int
    end_line: int


class ExtractionIssue(TypedDict):
    path: str
    chunk_id: str
    start_line: int
    end_line: int
    unverified_candidate_count: int


class NetworkState(TypedDict, total=False):
    input_dir: str
    output_path: str
    max_revision_rounds: int
    revision_round: int
    documents: list[SourceDocument]
    chunks: list[DocumentChunk]
    candidates: list[CandidateRecord]
    extraction_issues: list[ExtractionIssue]
    requirements: list[Requirement]
    discarded: list[DiscardedCandidate]
    review_findings: list[ReviewFinding]
    review_approved: bool
    run_id: str
