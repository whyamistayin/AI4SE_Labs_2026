# Repository Agent Guide

## Repository overview

This repository contains coursework for the AI4SE Labs 2026 course. The
assignments cover prompt engineering, requirements engineering, architecture
and design, implementation with retrieval-augmented generation, and
dissection of coding assistants.

## Main areas

- `Week_03_Prompting/`: prompt frameworks, retrieval evaluation, and metrics.
- `Week_04_Requirements/`: requirements extraction workflow, schemas, tests,
  and generated requirements output.
- `Week_05_Designing/`: architecture and design tasks, notes, reports, and
  source data.
- `Week_06_Implementation/`: repository chunking, embeddings, retrieval, RAG,
  and implementation reports.
- `Week_08_Dissecting/`: assignments examining coding-assistant capabilities,
  including instructions, prompts, skills, subagents, tools, and rules.
- `.github/`: repository-specific Copilot instructions, prompt files, and
  skills.

## Working guidelines

- Keep changes limited to the assignment or feature being worked on.
- Preserve existing reports and source data unless the task explicitly asks
  for changes.
- Follow the instructions in the nearest applicable `AGENTS.md` file.
- Use the existing tests and scripts when validating code changes.
- Do not add API keys, credentials, or other sensitive information.
- Prefer clear, concise documentation and preserve the existing file formats.

## Validation

For Python changes, run the focused tests or scripts associated with the
affected week and assignment. For documentation-only changes, review the
rendered Markdown and verify links and paths.
