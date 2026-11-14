"""Embed class chunks from Task 2 with Sentence Transformers."""

from __future__ import annotations

import argparse
import ast
import csv
import json
import math
import textwrap
from pathlib import Path
from typing import Any


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
CSV_FIELDS = (
    "model",
    "file",
    "class_name",
    "docstring",
    "method_names",
    "text",
    "embedding",
    "chunk",
)


def method_name(method_source: str, class_name: str) -> str:
    """Extract a method's name from its source string."""
    parsed = ast.parse(textwrap.dedent(method_source))
    for node in parsed.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            return node.name
    raise ValueError(f"Could not find a method definition in class {class_name}")


def class_text(class_chunk: dict[str, Any]) -> tuple[str, list[str]]:
    """Build the text representation to embed and return its method names."""
    class_name = class_chunk["name"]
    docstring = class_chunk.get("docstring") or ""
    method_names = [
        method_name(method_source, class_name)
        for method_source in class_chunk.get("methods", [])
    ]
    text = "\n".join(
        [
            f"Class: {class_name}",
            f"Description: {docstring}",
            f"Methods: {', '.join(method_names)}",
        ]
    )
    return text, method_names


def cosine_similarity(left: list[float], right: list[float]) -> float:
    """Return cosine similarity, rejecting invalid or incompatible vectors."""
    if len(left) != len(right) or not left:
        raise ValueError("embedding vectors must have the same non-zero length")
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0 or right_norm == 0:
        raise ValueError("embedding vectors must not be zero vectors")
    return sum(a * b for a, b in zip(left, right, strict=True)) / (left_norm * right_norm)


def create_embeddings(input_path: Path, output_path: Path, model: Any) -> None:
    """Embed each class and store its vector and original chunk in CSV."""
    chunks = json.loads(input_path.read_text(encoding="utf-8"))
    if not isinstance(chunks, list):
        raise ValueError("chunk file must contain a JSON list")

    records: list[dict[str, Any]] = []
    texts: list[str] = []
    for file_chunk in chunks:
        if not isinstance(file_chunk, dict) or not isinstance(file_chunk.get("classes"), list):
            raise ValueError("each file chunk must contain a classes list")
        for class_chunk in file_chunk["classes"]:
            if not isinstance(class_chunk, dict) or not isinstance(class_chunk.get("name"), str):
                raise ValueError("each class chunk must contain a class name")
            text, method_names = class_text(class_chunk)
            texts.append(text)
            records.append(
                {
                    "model": MODEL_NAME,
                    "file": file_chunk["file"],
                    "class_name": class_chunk["name"],
                    "docstring": class_chunk.get("docstring") or "",
                    "method_names": json.dumps(method_names, ensure_ascii=False),
                    "text": text,
                    "chunk": json.dumps(class_chunk, ensure_ascii=False),
                }
            )

    if not records:
        raise ValueError("no class chunks found in the input")

    embeddings = model.encode(
        texts,
        batch_size=32,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=CSV_FIELDS)
        writer.writeheader()
        for record, embedding in zip(records, embeddings, strict=True):
            record["embedding"] = json.dumps(embedding.tolist())
            writer.writerow(record)
    print(f"Wrote {len(records)} class embeddings to {output_path}")


def retrieve(query: str, store_path: Path, top_k: int, model: Any) -> None:
    """Rank stored class chunks by cosine similarity to a text query."""
    if top_k < 1:
        raise ValueError("--top-k must be at least 1")
    query_vector = model.encode(
        query,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=False,
    ).tolist()

    matches: list[dict[str, Any]] = []
    with store_path.open(encoding="utf-8", newline="") as store_file:
        reader = csv.DictReader(store_file)
        if reader.fieldnames is None or not set(CSV_FIELDS).issubset(reader.fieldnames):
            raise ValueError(f"embedding CSV is missing required columns: {store_path}")
        for row in reader:
            if row["model"] != MODEL_NAME:
                raise ValueError(
                    f"stored model {row['model']!r} does not match required model {MODEL_NAME!r}"
                )
            embedding = [float(value) for value in json.loads(row["embedding"])]
            score = cosine_similarity(query_vector, embedding)
            matches.append(
                {
                    "score": score,
                    "file": row["file"],
                    "class_name": row["class_name"],
                    "docstring": row["docstring"],
                    "method_names": json.loads(row["method_names"]),
                    "chunk": json.loads(row["chunk"]),
                }
            )

    matches.sort(key=lambda result: result["score"], reverse=True)
    print(json.dumps(matches[:top_k], indent=2, ensure_ascii=False))


def main() -> None:
    script_directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Create a CSV embedding store or retrieve relevant class chunks."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=script_directory.parent / "Task_2" / "chunks.json",
        help="Task 2 chunk JSON file (default: sibling Task_2/chunks.json)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=script_directory / "chunk_embeddings.csv",
        help="CSV embedding store (default: Task_3/chunk_embeddings.csv)",
    )
    parser.add_argument(
        "--query",
        help="Search the stored embeddings instead of creating them",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=5,
        help="Number of matching chunks to return (default: 5)",
    )
    args = parser.parse_args()

    from sentence_transformers import SentenceTransformer

    model = SentenceTransformer(MODEL_NAME)
    output_path = args.output.resolve()

    if args.query is not None:
        if not args.query.strip():
            parser.error("--query must not be blank")
        if not output_path.is_file():
            parser.error(f"embedding CSV does not exist: {output_path}")
        try:
            retrieve(args.query, output_path, args.top_k, model)
        except (ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
            parser.error(str(error))
    else:
        input_path = args.input.resolve()
        if not input_path.is_file():
            parser.error(f"chunk file does not exist: {input_path}")
        try:
            create_embeddings(input_path, output_path, model)
        except (ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
            parser.error(str(error))


if __name__ == "__main__":
    main()