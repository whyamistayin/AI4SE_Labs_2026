"""LangGraph workflow wiring for the requirements-refinement network."""

from langgraph.graph import END, START, StateGraph

from .extraction_node import extract_candidates
from .finalization_node import finalize_output
from .ingestion_node import ingest_documents
from .normalization_node import normalize_requirements
from .review_node import review_requirements
from .state import NetworkState


def _review_route(state: NetworkState) -> str:
    # Extraction gaps require source-level intervention, not normalization retries.
    if state.get("extraction_issues"):
        return "finish"
    max_rounds = state.get("max_revision_rounds", 2)
    if state.get("review_findings") and state.get("revision_round", 0) < max_rounds:
        return "revise"
    return "finish"


def build_network():
    graph = StateGraph(NetworkState)
    graph.add_node("ingest", ingest_documents)
    graph.add_node("extract", extract_candidates)
    graph.add_node("normalize", normalize_requirements)
    graph.add_node("review", review_requirements)
    graph.add_node("finalize", finalize_output)

    graph.add_edge(START, "ingest")
    graph.add_edge("ingest", "extract")
    graph.add_edge("extract", "normalize")
    graph.add_edge("normalize", "review")
    graph.add_conditional_edges(
        "review",
        _review_route,
        {"revise": "normalize", "finish": "finalize"},
    )
    graph.add_edge("finalize", END)
    return graph.compile()
