# Assessment by laguna-s-2.1

# Week 03 Prompting
- Awarded: 3b out of 5b
- Commentary: The student made a solid effort across all four tasks, producing well-structured prediction files and thoughtful prompt frameworks. However, several deliverables are incomplete: Task 2 lacks a comparison report, visualization, and inference time measurements; Task 3 proposes an original metric but does not implement it or provide a detailed implementation guide; Task 4 provides brief qualitative analysis but omits required tables, graphs, and statistical significance testing.

## Task 1
- Awarded: 1b   (max 1b)
- Commentary: The student selected three prompting frameworks (APE, STAR, GENERAL) from frompting.com, explicitly excluding ROSES and zero-shot as required. A well-formatted data file (prompts_frameworks.txt) contains three substantial prompts, each clearly following its respective framework structure and targeting the same problem domain (penguin logistic regression). A brief report (report.txt) explains the rationale for each framework choice and what outcome is expected. All required outputs are present and properly structured.

## Task 2
- Awarded: 0.5b   (max 1b)
- Commentary: The student generated prediction files (star.csv, ape.csv, general.csv) for all three prompt frameworks, each with the required columns (question, predicted_sql, model, template) and proper metadata. The original prompt files are also stored. However, the task explicitly required a brief comparison report, a visualization, and inference time measurements, none of which are present in the Task 2 deliverables. The prediction files themselves are comprehensive and well-formed, but the reporting and analysis components are missing.

## Task 3
- Awarded: 0.5b   (max 1b)
- Commentary: The student proposed an original and creative metric: comparing SQL queries semantically using Jaccard similarity against reference "ideal" queries, with scores in a continuous [0, 1] range rather than binary pass/fail. The metric.txt file argues why this is a good and applicable metric and discusses preprocessing considerations (e.g., normalizing AS aliases). However, the student did not implement the metric calculation, did not calculate values for the Task 2 predictions, and the alternative output of a detailed implementation guide is not provided — the discussion remains conceptual rather than a step-by-step implementation guide.

## Task 4
- Awarded: 1b   (max 2b)
- Commentary: The student's report.txt identifies key findings (APE achieving 27% accuracy while GENERAL and STAR failed with SQL syntax errors) and offers some qualitative reasoning about why APE performed best. However, the task required detailed analysis with tables, graphs/demonstrations, and statistical significance testing — none of which are present. The report is brief and reads more like notes than a detailed analysis. The required consideration of prompts, model, and coding agent as factors is also absent. Some meaningful results are reported but the analysis format and depth fall well short of the requirements.
