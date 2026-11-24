# Assessment by mimo-2.6-flash

# Week 03 Prompting
- Awarded: 2b out of 5b
- Commentary: All four tasks produced some artefact, but almost every deliverable is only partially fulfilled: the reports are a handful of lines, the mandated comparison report, visualisation and inference-time measurements for Task 2 are missing entirely, Task 3 was never implemented or calculated, and Task 4 lacks tables, graphs and statistical testing. No images/plots exist in the submission, so there was nothing to view beyond the plain-text reports.

## Task 1
- Awarded: 0.5b   (max 1b)
- Commentary: Three frameworks (APE, STAR, General) were chosen from https://frompting.com/frameworks without using ROSES, and a prompt file (prompts_frameworks.txt) plus a report citing the source were delivered. However, the justification is four very terse lines ("it is a great reference", "it is said it gives clear instructions"), the explicitly required expectations ("what do you expect from it") are essentially absent, and the formulated prompts target a palmerpenguins/logistic-regression task rather than Task 2's SQL-generation problem, so the promised link to Task 2 was not honoured literally (only loosely, via re-written prompts in Task 2 that mimic the same structures). "General" is also asserted as a framework without showing its definition from the source site.

## Task 2
- Awarded: 0.5b   (max 1b)
- Commentary: Prediction files for all three prompts exist (ape.csv, star.csv, general.csv / restaurants_dataset_predictions.csv, 155 questions each) with question, predicted_sql, model and template columns, and an evaluator script is present. But the required brief comparison report, the "nice visualisation", and the inference-time measurements are all missing (no report file, no plot/image, no timings anywhere in the folder), the root-level evaluate_retrieval_predictions.csv is empty, and the prompt metadata is unusable: the template column literally reads "General" in every file (including ape.csv and star.csv), and restaurants_dataset_predictions.csv is byte-wise identical in sampled head/tail to star.csv, so runs cannot be reliably attributed to prompts.

## Task 3
- Awarded: 0.5b   (max 1b)
- Commentary: A metric is proposed and defended at a conceptual level - semantic similarity of the generated SQL to a ground-truth query via the Jaccard index on a [0,1] scale, averaged per prompt, explicitly motivated as a complement/replacement for the brittle 0/1 execution accuracy, including a genuinely pertinent normalization caveat (aliases such as "AS y" inflating distance). However, the student states outright that it was not implemented, there is no source code, no metric values computed on the Task 2 predictions, and no report comparing prompts; the fallback "detailed guide" of the ALTERNATIVE OUTPUT is only a short sketch without procedure, parsing/normalisation steps, or examples.

## Task 4
- Awarded: 0.5b   (max 2b)
- Commentary: The 19-line report gives only a rough summary of results - APE ~27%, GENERAL and STAR treated as 0% because the evaluator crashed on line 2 of restaurants_dataset_predictions.csv - plus a plausible high-level interpretation (STAR is narrative, so poorly suited to precise technical instructions; APE expected to win). Everything else demanded by the task is absent: no tables, no graphs, no statistical-significance test of the metric differences, and no analysis of the model or coding agent as factors. The analysis is also technically shallow: the crash reflects Oracle-style "FETCH FIRST ... ROW ONLY" statements failing against SQLite (an SQL-dialect/evaluation-harness issue, compounded by the duplicated star/predictions file) rather than proof that the model "failed to generate correct syntax", and no stored accuracy artefacts (the results CSV is empty) back the 27%/0% figures.