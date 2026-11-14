# Chunking design

The script uses Python's built-in `ast` module to identify top-level classes,
their direct methods, and top-level functions. Each class chunk keeps the class
name, docstring, and methods together, so a retrieved method retains its class
context. Methods are stored as source strings, with line bounds on each class
and top-level function. Class-level statements, module-level statements, and
top-level functions are also retained rather than discarded.

The natural chunk unit is a class, with each method separately represented
inside its class entry; standalone functions are their own entries. This keeps
related methods associated without splitting at arbitrary blank lines. Chunk
size therefore follows code structure instead of a fixed line or token limit.
A very large method or class can still produce a large chunk; it could be split
further if later retrieval or context-window limits require it.

Only `.py` files are processed. Version-control, virtual-environment, generated,
and dependency directories are skipped. The result is `chunks.json`, a
human-readable JSON list that preserves repository-relative file paths for
traceability.

Run from any working directory:

```bash
python Task_2/chunk_repository.py
```

By default, the script reads `AI4SE_Playground` beside `Task_2` and writes
`Task_2/chunks.json`. Use `--source` and `--output` to override those paths.
