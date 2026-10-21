"""Structured data contracts shared by the graph's LLM nodes."""

from typing import Literal

from pydantic import BaseModel, Field


Priority = Literal["Must", "Should", "Could"]


class CandidateRequirement(BaseModel):
    name: str = Field(min_length=1, description="Short, specific requirement name.")
    description: str = Field(
        min_length=1,
        description="A self-contained paragraph describing the required behavior.",
    )
    priority: Priority = Field(description="Suggested MoSCoW priority.")
    evidence: str = Field(
        min_length=1,
        description="A concise verbatim excerpt supporting this candidate."
    )


class ExtractionResult(BaseModel):
    requirements: list[CandidateRequirement] = Field(
        description="Atomic, software-related requirement candidates in the text."
    )


class SourceReference(BaseModel):
    candidate_id: str = Field(
        min_length=1,
        description="Exact candidate_id copied from an extracted candidate.",
    )


class Requirement(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    priority: Priority
    sources: list[SourceReference] = Field(min_length=1)


class DiscardedCandidate(BaseModel):
    name: str = Field(min_length=1)
    description: str = Field(min_length=1)
    reason: str = Field(min_length=1)
    sources: list[SourceReference] = Field(min_length=1)


class NormalizationResult(BaseModel):
    requirements: list[Requirement]
    discarded: list[DiscardedCandidate]


class ReviewFinding(BaseModel):
    severity: Literal["high", "medium", "low"]
    affected_requirement_names: list[str] = Field(default_factory=list)
    explanation: str = Field(min_length=1)
    recommended_action: str = Field(min_length=1)


class ReviewResult(BaseModel):
    approved: bool
    findings: list[ReviewFinding] = Field(default_factory=list)
