---
name: python-debugging
description: "Use when investigating Python bugs or reviewing Python code for likely defects, especially type errors, circular imports, or weak encapsulation."
argument-hint: "Python file, error message, traceback, or debugging question"
---

# Python Debugging

Investigate the cause of Python defects and recommend or implement the smallest
reliable fix. Ground conclusions in the actual code and observed errors; do not
guess at runtime behavior when it can be checked.

## Workflow

1. Read the relevant code, nearby tests, and project configuration before
   proposing changes. Trace the failing value or call through its callers and
   dependencies.
2. Reproduce the issue with the narrowest available test or command. If it
   cannot be reproduced, distinguish confirmed facts from hypotheses and state
   what evidence is missing.
3. Check for these common problem areas:
   - **Type errors:** Compare annotations with actual values and call sites.
     Check optional values, incompatible return types, generic/container
     element types, overrides, and values crossing parsing or I/O boundaries.
     Distinguish static type-checker findings from runtime exceptions. Use the
     repository's configured checker when available; do not silence errors with
     broad casts or weakened annotations without justification.
   - **Circular imports:** Trace module-level imports in both directions and
     identify the cycle and the symbol needed at import time. Prefer moving
     shared definitions to a lower-level module, using local imports only when
     they are genuinely appropriate, or restructuring dependencies. Do not
     disguise a cycle with broad exception handling or partially initialized
     module state.
   - **Encapsulation:** Check whether callers directly modify internal or
     mutable state, bypass validation, or depend on implementation details.
     Identify invariants that can be broken. Prefer a small public method or
     property that preserves those invariants; avoid adding wrappers or
     underscore conventions that do not improve control or clarity.
   - **Other likely causes:** Inspect boundary validation, exception handling,
     resource lifetime, mutation, and assumptions that disagree with tests or
     documented behavior.
4. Explain the root cause and why it produces the observed behavior. Keep the
   fix focused; preserve existing behavior except where the bug requires a
   change.
5. Add or update a focused regression test when making a code fix. Run that
   test and any directly relevant type checker or test suite. Report commands
   run and results accurately.

## Guidance

- Do not claim a bug is fixed unless the relevant check passes.
- Do not hide failures with broad catches, silent defaults, or skipped tests.
- Separate unrelated findings from the requested fix.
- When suggesting alternatives, state their trade-offs and prefer the simplest
  design that makes the defect difficult to reintroduce.
