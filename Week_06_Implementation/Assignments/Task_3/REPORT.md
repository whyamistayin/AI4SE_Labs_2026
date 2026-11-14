# Task 3: Embedding and retrieval design

## Embedding representation

The script uses the pretrained
`sentence-transformers/all-MiniLM-L6-v2` model. For each class chunk from
`Task_2/chunks.json`, it embeds a short text containing the class name,
docstring, and method names. This representation focuses on the class's
purpose and available operations, while avoiding embedding all method bodies.
The model produces a 384-dimensional vector. Vectors are normalized when
created, and the same model and normalization are used for search queries.

## Storage

The script writes one row per class to `chunk_embeddings.csv`. CSV was chosen
because it is simple, portable, and inspectable without a separate database.
Each row stores the model name, repository-relative file path, class name,
docstring, method names, embedded text, embedding vector, and original class
chunk. The method-name list, vector, and original chunk are JSON-encoded in
their respective CSV cells so their structure can be reconstructed when read.

The saved original chunk allows retrieval to return the class context, not only
an embedding or identifier. Storing the model name alongside each row also
makes the vector's origin explicit and lets retrieval reject incompatible
models.

## Retrieval

For a coding task, the script embeds the query with the same model, reads the
stored vectors, calculates cosine similarity, and returns the top `k` matching
class chunks (five by default). This linear scan is easy to understand and is
adequate for the small lab repository. A larger collection could use a vector
index or vector database for faster nearest-neighbor search.

## Running

Install `sentence-transformers` in the Python environment used to run the
script, then generate the CSV store:

```bash
python -m pip install sentence-transformers
python Task_3/embed_chunks.py
```

Search the generated store with a coding task:

```bash
python Task_3/embed_chunks.py --query "How are product prices validated?" --top-k 5
```

By default, the script reads `Task_2/chunks.json` and writes
`Task_3/chunk_embeddings.csv`. Use `--input` and `--output` to select different
paths. The first model load may download the model files.

This implementation indexes class chunks only. Although Task 2 also records
top-level functions and module-level code, those are not currently embedded or
returned by this Task 3 script.