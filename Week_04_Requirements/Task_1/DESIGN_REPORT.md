# Requirements Network Design Report

## Purpose and inputs

The network turns a directory of software-related source documents into a
traceable, prioritized requirements specification. It recursively discovers
`.txt` and `.eml` files; paths are supplied at runtime rather than embedded in
the implementation. Email messages are parsed with Python's standard email
library, and text is chunked with overlap so long documents fit model contexts
without losing source path and line-range provenance. This map–reduce structure
lets extraction process documents independently before the network consolidates
evidence across the full corpus. It also avoids assuming that one document
contains the entire or authoritative version of a requirement.

## LangGraph nodes

1. **Ingestion (`ingestion_node.py`, deterministic):** validates the input
   directory, reads supported files, assigns stable document identifiers, and
   creates provenance-aware chunks. Files larger than 5 MiB and empty input
   directories produce explicit errors. Stable IDs and retained line ranges
   provide a reliable way to trace claims back to their original files, while
   chunk overlap reduces the chance of losing context when a statement falls
   near a chunk boundary.
2. **Extraction (`extraction_node.py`, `gpt-6-luna`):** extracts atomic,
   evidence-supported candidates from each chunk. It returns structured data
   and treats source contents as untrusted evidence. Processing chunks
   separately also makes the source of each candidate explicit; quoted
   evidence is checked against the chunk before the candidate is kept. The
   check tolerates punctuation and whitespace differences but requires an exact
   contiguous word sequence; if it fails, extraction retries once with a
   stricter instruction. Candidates whose evidence remains unverifiable are
   excluded individually, while the remaining verified candidates continue
   through the graph. Their source ranges are recorded as extraction gaps in
   the review and final document, so the run does not silently claim complete
   coverage.
3. **Normalization (`normalization_node.py`, `gpt-5.4-nano`):** merges semantic
   duplicates, harmonizes vocabulary and priority, and explicitly lists
   discarded, conflicting, or nonsensical candidates with their provenance.
   This cross-document step is necessary because different stakeholders may
   describe the same behavior using different terms, or may express
   contradictory expectations. Keeping rejected candidates and reasons makes
   these decisions auditable rather than silently losing source information.
   Its structured-output schema dynamically limits citations to the candidate
   IDs extracted for that run. Finalization independently checks those IDs
   against the extraction inventory, so invented IDs are rejected before an
   untraceable requirement can be written.
4. **Independent review (`review_node.py`, `gpt-5.6-luna`):** checks coverage,
   traceability, duplicate handling, clarity, consistency, and conflicts
   against both the source inventory and extracted candidates. Using a separate
   model role gives the review stage a distinct task from extraction and
   consolidation; it checks whether requirements reflect the gathered evidence
   rather than simply accepting the normalizer's output.
5. **Feedback loop:** actionable review findings route back to normalization.
   The loop is bounded by `--max-revision-rounds` (two by default); unresolved
   findings are surfaced in the generated document. The bound limits repeated
   model calls and prevents a review cycle from running indefinitely, while
   still giving the normalizer a chance to address clear omissions or
   inconsistencies. Extraction gaps are reported for manual source inspection
   and do not cause futile normalization retries.
6. **Finalization (`finalization_node.py`, deterministic):** checks source
   references and duplicate requirement text, assigns stable ordered IDs, and
   writes one structured Markdown document. These deterministic checks catch
   malformed or unsupported citations before output and ensure the final
   document follows a consistent structure independent of model wording.
   Each extracted candidate receives a per-run unique ID. The normalizer refers to
   those IDs rather than rewriting source quotes or line metadata; finalization
   resolves the IDs to extractor-verified evidence and renders the exact source
   wording. This avoids trusting the normalizer to reproduce citations
   correctly.

The graph therefore uses three LLM-invoking nodes, three distinct configured
models, deterministic nodes, and a conditional feedback cycle.

## Design trade-offs

The network uses LLMs for tasks requiring semantic interpretation—extracting
requirements, recognizing duplicates and conflicts, and reviewing completeness.
File discovery, source IDs, structural validation, and output formatting remain
deterministic so these operations are repeatable and easier to test. Structured
Pydantic responses constrain model output to the fields downstream nodes
expect. Model names are configurable through environment variables because
availability can differ between environments. The network uses `gpt-6-luna`
for evidence-focused extraction, `gpt-5.4-nano` for cross-document
normalization, and `gpt-5.6-luna` for independent review. This allocates the
strongest selected model to extraction and review, where missing or
misinterpreted requirements most affect downstream quality, while keeping
normalization on a distinct model for duplicate and conflict analysis.

Chunk-level extraction makes the workflow suitable for a corpus larger than a
single model context, but completeness still depends on model quality and
review. The review loop therefore records unresolved findings rather than
claiming that every corpus requirement has been captured. The final document
also preserves supporting quotations and rejected candidates so a reader can
verify important decisions against the source material.

## Output contract

The generated Markdown specifies a MoSCoW priority scale (Must, Should, Could),
unique `REQ-NNN` identifiers, names, explanatory paragraphs, source paths,
document IDs, chunk IDs, line ranges, and supporting quotations. A separate
section records discarded or conflicting candidates and reasons. Findings
remaining after the configured revision limit are included in that same
document; the network does not claim review approval in that case.

## Configuration and operation

Install dependencies with `python3 -m pip install -r requirements.txt`. Set
`API_KEY` in the process environment to a newly issued credential, for example
with `export API_KEY="..."` in a POSIX shell. The credential is never read from
a source file, printed, or written to the output.
The three model names can be overridden with `EXTRACTION_MODEL`,
`NORMALIZATION_MODEL`, and `REVIEW_MODEL`; an OpenAI-compatible base URL may be
provided using `OPENAI_BASE_URL`. Request timeouts can be set globally with
`OPENAI_TIMEOUT_SECONDS` or per node with `EXTRACT_TIMEOUT_SECONDS`,
`NORMALIZE_TIMEOUT_SECONDS`, and `REVIEW_TIMEOUT_SECONDS`. Normalization has a
longer default timeout because it consolidates all extracted candidates in one
structured response. API retries are bounded and configurable with
`OPENAI_MAX_RETRIES`; timeouts that persist after retries remain explicit
errors rather than being treated as successful results.

Run the example corpus with:

```sh
python3 run_requirements.py \
  --input-dir data/corpus \
  --output output/requirements.md
```

The generated report is kept under the ignored `output/` directory so
model-generated content and potentially sensitive corpus material are not
added to version control by accident. API credentials should never be
committed.
