# Task 5: RAG implementation and test report

## Implementation

`run_rag.py` accepts a single textual implementation task or reads all entries
from `missing_code.json`. For each target method, it embeds the task with the
Task 3 sentence-transformer model, retrieves the five closest class chunks
using Task 4's cosine-similarity helper, and sends the task, target class,
current method, and retrieved chunks to an OpenAI-compatible chat-completions
endpoint. The model is selected from the list allowed by the assignment.

The script reads the API credential from `API_KEY` and never writes or prints
it. `OPENAI_BASE_URL` may be set for a compatible model endpoint; otherwise,
the standard OpenAI API base URL is used. It does not force a sampling
temperature, allowing GPT-5 endpoints to use their supported default. Responses
are required to contain exactly one method with the existing method name,
parameters, and return annotation. The original signature and docstring are
preserved, and all generated updates are parsed before any target file is
written. Target paths are constrained to the cloned repository. HTTP errors
report a bounded API diagnostic message, when available, without printing the
credential.

## Usage

With `API_KEY` set in the process environment and `Task_3/chunk_embeddings.csv`
generated:

```bash
python Task_5/run_rag.py
```

To solve one textual task instead:

```bash
python Task_5/run_rag.py \
  --task "Return whether a money amount is non-zero." \
  --target-file playground/playground/models.py \
  --class-name Money \
  --method-name __bool__
```

Use `--model` to choose another allowed model, and `--store` to select a
different embedding CSV.

## Test results

The RAG script passed syntax validation and a mocked end-to-end test that
exercised the embedding-to-retrieval handoff, method-signature preservation,
docstring preservation, and writing a generated implementation. The retrieval
helper was separately tested against the stored CSV vectors. The mock test did
not make a real LLM request, and no live LLM request has been verified.

All ten methods listed in `missing_code.json` were implemented in the cloned
repository. The complete test suite was run afterward:

```text
Ran 481 tests
OK
```

An earlier baseline run before those implementations reported 35 failures and
17 errors. The test suite passed after implementation.

The API credential was pasted into chat and was not used for a live LLM call.
The RAG pipeline is implemented and its flow was tested with a mock model
response; the ten requested methods were completed locally rather than
generated through that live pipeline. Revoke/rotate the exposed credential
before using the script with a replacement configured in the environment.
