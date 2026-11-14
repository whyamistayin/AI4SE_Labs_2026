"""Retrieve the most relevant chunks from the Task 3 embedding CSV."""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path
from typing import Any


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
REQUIRED_FIELDS = {
    "model",
    "file",
    "class_name",
    "docstring",
    "method_names",
    "embedding",
    "chunk",
}


def load_query_vector(path: Path) -> list[float]:
    """Load a numeric embedding from a JSON array or an object with `embedding`."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("embedding")
    if not isinstance(data, list) or not data:
        raise ValueError("query embedding JSON must contain a non-empty numeric array")
    if any(isinstance(value, bool) or not isinstance(value, (int, float)) for value in data):
        raise ValueError("query embedding must contain only numbers")
    vector = [float(value) for value in data]
    if any(not math.isfinite(value) for value in vector):
        raise ValueError("query embedding values must be finite")
    return vector


def cosine_similarity(left: list[float], right: list[float]) -> float:
    """Calculate cosine similarity for two vectors."""
    if len(left) != len(right):
        raise ValueError(
            f"embedding dimensions do not match ({len(left)} != {len(right)})"
        )
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0 or right_norm == 0:
        raise ValueError("embedding vectors must not be zero vectors")
    return sum(a * b for a, b in zip(left, right, strict=True)) / (
        left_norm * right_norm
    )


def retrieve_chunks(
    query_vector: list[float], store_path: Path, top_k: int
) -> list[dict[str, Any]]:
    """Return up to `top_k` stored chunks ranked by cosine similarity."""
    if top_k < 1:
        raise ValueError("top-k must be at least 1")
    if not query_vector or any(not math.isfinite(value) for value in query_vector):
        raise ValueError("query embedding must be a non-empty finite vector")

    matches: list[dict[str, Any]] = []
    with store_path.open(encoding="utf-8", newline="") as store_file:
        reader = csv.DictReader(store_file)
        if reader.fieldnames is None or not REQUIRED_FIELDS.issubset(reader.fieldnames):
            missing = REQUIRED_FIELDS - set(reader.fieldnames or [])
            raise ValueError(f"embedding CSV is missing required columns: {', '.join(sorted(missing))}")

        for line_number, row in enumerate(reader, start=2):
            if row["model"] != MODEL_NAME:
                raise ValueError(
                    f"row {line_number} uses model {row['model']!r}; expected {MODEL_NAME!r}"
                )
            try:
                embedding_data = json.loads(row["embedding"])
                chunk = json.loads(row["chunk"])
                method_names = json.loads(row["method_names"])
            except json.JSONDecodeError as error:
                raise ValueError(f"invalid JSON in embedding CSV row {line_number}") from error
            if not isinstance(embedding_data, list) or any(
                isinstance(value, bool) or not isinstance(value, (int, float))
                for value in embedding_data
            ):
                raise ValueError(f"invalid embedding vector in CSV row {line_number}")
            embedding = [float(value) for value in embedding_data]
            if any(not math.isfinite(value) for value in embedding):
                raise ValueError(f"non-finite embedding value in CSV row {line_number}")
            if not isinstance(chunk, dict) or not isinstance(method_names, list):
                raise ValueError(f"invalid chunk metadata in CSV row {line_number}")

            matches.append(
                {
                    "score": cosine_similarity(query_vector, embedding),
                    "file": row["file"],
                    "class_name": row["class_name"],
                    "docstring": row["docstring"],
                    "method_names": method_names,
                    "chunk": chunk,
                }
            )

    if not matches:
        raise ValueError("embedding CSV contains no chunk rows")
    matches.sort(key=lambda result: (-result["score"], result["file"], result["class_name"]))
    return matches[:top_k]


def main() -> None:
    task_3_directory = Path(__file__).resolve().parent.parent / "Task_3"
    parser = argparse.ArgumentParser(
        description="Find the top matching code chunks from a Task 3 embedding CSV."
    )
    query_source = parser.add_mutually_exclusive_group(required=True)
    query_source.add_argument(
        "--query",
        help="Task description to embed using the Task 3 sentence-transformer model",
    )
    query_source.add_argument(
        "--query-embedding",
        type=Path,
        help="JSON file containing a precomputed query vector (array or {\"embedding\": [...]})",
    )
    parser.add_argument(
        "--store",
        type=Path,
        default=task_3_directory / "chunk_embeddings.csv",
        help="Task 3 CSV embedding store (default: sibling Task_3/chunk_embeddings.csv)",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of chunks to return (default: 5)",
    )
    args = parser.parse_args()

    store_path = args.store.resolve()
    if not store_path.is_file():
        parser.error(f"embedding CSV does not exist: {store_path}")
    if args.top_k < 1:
        parser.error("--top-k must be at least 1")

    try:
        if args.query_embedding is not None:
            query_path = args.query_embedding.resolve()
            if not query_path.is_file():
                parser.error(f"query embedding file does not exist: {query_path}")
            query_vector = load_query_vector(query_path)
        else:
            if not args.query.strip():
                parser.error("--query must not be blank")
            from sentence_transformers import SentenceTransformer

            model = SentenceTransformer(MODEL_NAME)
            query_vector = model.encode(
                args.query,
                convert_to_numpy=True,
                normalize_embeddings=True,
                show_progress_bar=False,
            ).tolist()

        results = retrieve_chunks(query_vector, store_path, args.top_k)
    except (ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        parser.error(str(error))

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
