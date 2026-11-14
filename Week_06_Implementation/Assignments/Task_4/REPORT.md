# Task 4: Embedding matching design

The retrieval script compares an input task embedding with the vectors stored
in `Task_3/chunk_embeddings.csv`. For convenience, it accepts task text and
embeds it with the same `sentence-transformers/all-MiniLM-L6-v2` model used to
build the store. It also accepts a precomputed query embedding as a JSON array,
so matching can be run separately from embedding generation.

The script uses cosine similarity to measure vector direction (semantic
similarity) and returns the top `k` rows, five by default. Each result includes
its score, file and class metadata, and the original class chunk, making it
ready to provide to a later generation step. The vectors are scanned directly
from CSV, which is simple and sufficient for this small repository; a larger
collection could use an approximate-nearest-neighbor index.

The CSV row records the model name. The matcher checks that it matches the
expected model and that vector dimensions agree. For a manually supplied query
vector, generate it with the same model and normalized-embedding setting as
the stored vectors.

## Usage

Generate or update the embedding CSV with Task 3, then retrieve chunks by task
description:

```bash
python Task_4/retrieve_chunks.py --query "How does the customer credit limit work?" --top-k 5
```

Or match a vector saved as a JSON array (or as an object containing an
`embedding` array):

```bash
python Task_4/retrieve_chunks.py --query-embedding query_embedding.json --top-k 3
```

The store defaults to `Task_3/chunk_embeddings.csv`. Override it with
`--store` if the CSV is elsewhere. Text queries require the `sentence-transformers`
package and the model files; precomputed-vector matching uses only the Python
standard library.
