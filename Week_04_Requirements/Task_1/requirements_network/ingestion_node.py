"""Deterministic corpus discovery, parsing, and provenance-preserving chunking."""

import hashlib
import os
from email import policy
from email.parser import BytesParser
from pathlib import Path

from .state import DocumentChunk, NetworkState, SourceDocument


SUPPORTED_SUFFIXES = {".txt", ".eml"}
MAX_DOCUMENT_BYTES = 5 * 1024 * 1024
DEFAULT_CHUNK_CHARS = 12_000
DEFAULT_OVERLAP_CHARS = 800


def _text_from_email(path: Path) -> str:
    message = BytesParser(policy=policy.default).parsebytes(path.read_bytes())
    parts = [
        part.get_content()
        for part in message.walk()
        if part.get_content_type() == "text/plain"
        and not part.get_content_disposition() == "attachment"
    ]
    if parts:
        header = "\n".join(
            f"{name}: {message.get(name)}"
            for name in ("From", "To", "Date", "Subject")
            if message.get(name)
        )
        return f"{header}\n\n" + "\n\n".join(str(part) for part in parts)
    return message.as_string()


def _read_document(path: Path) -> str:
    if path.stat().st_size > MAX_DOCUMENT_BYTES:
        raise ValueError(f"Document exceeds the 5 MiB limit: {path}")
    if path.suffix.lower() == ".eml":
        text = _text_from_email(path)
    else:
        text = path.read_text(encoding="utf-8-sig")
    return text.replace("\r\n", "\n").replace("\r", "\n")


def _document_id(relative_path: str) -> str:
    digest = hashlib.sha256(relative_path.encode("utf-8")).hexdigest()[:12]
    return f"DOC-{digest}"


def _chunk_document(
    document: SourceDocument,
    chunk_chars: int = DEFAULT_CHUNK_CHARS,
    overlap_chars: int = DEFAULT_OVERLAP_CHARS,
) -> list[DocumentChunk]:
    if chunk_chars <= 0 or not 0 <= overlap_chars < chunk_chars:
        raise ValueError("Chunk size must be positive and overlap smaller than size.")
    lines = document["text"].splitlines()
    segments = [
        (line_number, line[offset : offset + chunk_chars])
        for line_number, line in enumerate(lines, start=1)
        for offset in range(0, max(len(line), 1), chunk_chars)
    ]
    chunks: list[DocumentChunk] = []
    start = 0
    while start < len(segments):
        end = start
        size = 0
        while end < len(segments):
            line_size = len(segments[end][1]) + (1 if end > start else 0)
            if end > start and size + line_size > chunk_chars:
                break
            size += line_size
            end += 1
        text = "\n".join(text for _, text in segments[start:end])
        chunks.append(
            {
                "chunk_id": f'{document["document_id"]}-C{len(chunks) + 1:03d}',
                "document_id": document["document_id"],
                "path": document["path"],
                "start_line": segments[start][0],
                "end_line": segments[end - 1][0],
                "text": text,
            }
        )
        if end >= len(segments):
            break
        rewind = 0
        next_start = end
        while next_start > start + 1 and rewind < overlap_chars:
            next_start -= 1
            rewind += len(segments[next_start][1]) + 1
        start = next_start
    return chunks


def ingest_documents(state: NetworkState) -> dict:
    input_dir = Path(state["input_dir"]).expanduser().resolve()
    if not input_dir.is_dir():
        raise NotADirectoryError(f"Input directory does not exist: {input_dir}")

    documents: list[SourceDocument] = []
    for path in sorted(input_dir.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue
        if path.is_symlink():
            continue
        relative_path = path.relative_to(input_dir).as_posix()
        documents.append(
            {
                "document_id": _document_id(relative_path),
                "path": relative_path,
                "text": _read_document(path),
            }
        )
    if not documents:
        raise ValueError(
            f"No .txt or .eml documents found in input directory: {input_dir}"
        )

    chunk_chars = int(os.environ.get("CHUNK_SIZE_CHARS", DEFAULT_CHUNK_CHARS))
    overlap_chars = int(os.environ.get("CHUNK_OVERLAP_CHARS", DEFAULT_OVERLAP_CHARS))
    chunks = [
        chunk
        for document in documents
        for chunk in _chunk_document(document, chunk_chars, overlap_chars)
    ]
    return {"documents": documents, "chunks": chunks}
