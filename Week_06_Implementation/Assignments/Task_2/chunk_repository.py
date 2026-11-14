"""Group Python source files into JSON chunks by class and method."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
from typing import Any


IGNORED_DIRECTORIES = {
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "venv",
}


def source_for(source_lines: list[str], node: ast.AST) -> str:
    """Return the exact source lines covered by an AST node."""
    return "".join(source_lines[start_line(node) - 1 : node.end_lineno]).rstrip()


def start_line(node: ast.AST) -> int:
    """Return a definition's first decorator line, or its own line."""
    return min(
        [node.lineno, *(decorator.lineno for decorator in getattr(node, "decorator_list", []))]
    )


def chunk_file(path: Path, repository_root: Path) -> dict[str, Any]:
    """Represent one Python file as its classes, functions, and module statements."""
    source = path.read_text(encoding="utf-8")
    source_lines = source.splitlines(keepends=True)
    tree = ast.parse(source, filename=str(path))

    classes: list[dict[str, Any]] = []
    functions: list[dict[str, Any]] = []
    module_code: list[str] = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            methods = [
                source_for(source_lines, member)
                for member in node.body
                if isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef))
            ]
            class_docstring = ast.get_docstring(node, clean=False)
            class_code = [
                source_for(source_lines, member)
                for member in node.body
                if not isinstance(member, (ast.FunctionDef, ast.AsyncFunctionDef))
                and not (
                    isinstance(member, ast.Expr)
                    and isinstance(member.value, ast.Constant)
                    and isinstance(member.value.value, str)
                    and member is node.body[0]
                )
            ]
            classes.append(
                {
                    "name": node.name,
                    "start_line": start_line(node),
                    "end_line": node.end_lineno,
                    "docstring": class_docstring,
                    "bases": [ast.get_source_segment(source, base) for base in node.bases],
                    "decorators": [
                        ast.get_source_segment(source, decorator) for decorator in node.decorator_list
                    ],
                    "methods": methods,
                    "class_code": class_code,
                }
            )
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append(
                {
                    "name": node.name,
                    "start_line": start_line(node),
                    "end_line": node.end_lineno,
                    "source": source_for(source_lines, node),
                }
            )
        else:
            module_code.append(source_for(source_lines, node))

    return {
        "file": path.relative_to(repository_root).as_posix(),
        "classes": classes,
        "functions": functions,
        "module_code": module_code,
    }


def python_files(repository_root: Path):
    """Yield Python files while skipping generated and environment directories."""
    for path in sorted(repository_root.rglob("*.py")):
        if not any(part in IGNORED_DIRECTORIES for part in path.relative_to(repository_root).parts):
            yield path


def main() -> None:
    script_directory = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(
        description="Chunk a Python repository into class- and function-based JSON."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=script_directory.parent / "AI4SE_Playground",
        help="Python repository to process (default: sibling AI4SE_Playground directory)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=script_directory / "chunks.json",
        help="JSON output path (default: Task_2/chunks.json)",
    )
    args = parser.parse_args()

    repository_root = args.source.resolve()
    if not repository_root.is_dir():
        parser.error(f"source repository does not exist or is not a directory: {repository_root}")

    chunks = [chunk_file(path, repository_root) for path in python_files(repository_root)]
    output_path = args.output.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(chunks, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(chunks)} Python file chunks to {output_path}")


if __name__ == "__main__":
    main()
