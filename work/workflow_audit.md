# FL-01: Workflow Audit & AI Toolkit Setup

- **Author:** FlyRank ML Intern
- **Track:** AI Fluency Track (Phase: Setup)
- **Repo:** [github.com/ridaeman02/flyrank-ml-internship](https://github.com/ridaeman02/flyrank-ml-internship)
- **Date:** 2026-08-07

---

## 1. Weekly Workflow Audit Table

Below is an audit of 12 recurring tasks from my real weekly workflow across machine learning coursework, coding, data analysis, and professional communication. Each task is classified using Ethan Mollick's task-classification framework.

| # | Task Description | Category | One-Line Rationale |
|---|---|---|---|
| 1 | **High-Stakes Client Strategic Alignment & Mentorship Check-ins** | **Just Me** | High emotional intelligence, nuanced trust-building, and personal accountability cannot be delegated to an AI model. |
| 2 | **Final Quality Control & Ethical Judgment on ML Models** | **Just Me** | Accountability for model bias, data leakage claims, and final deployment safety rests entirely on human engineering judgment. |
| 3 | **DuckDB SQL Query Construction for Large Parquet Slices** | **Collaborate with AI** | AI drafts complex window functions and CTEs rapidly, while I provide schema context and verify query execution logic. |
| 4 | **Python Code Refactoring & Docstring Generation** | **Delegate to AI with Review** | AI excels at standardizing PEP-8 styles and writing docstrings, requiring only a quick human sanity check. |
| 5 | **ML Baseline Model Boilerplate Setup (scikit-learn)** | **Delegate to AI with Review** | Generating standard imports, model instantiation, and train-test split skeletons is repetitive and easily verified. |
| 6 | **Research Paper Literature Summarization & Key Finding Audits** | **Collaborate with AI** | AI synthesizes methodology sections quickly, while I critically evaluate assumptions, dataset limitations, and claims. |
| 7 | **Weekly Progress Report & Executive Summary Drafting** | **Collaborate with AI** | AI structures bullet points into professional 3-sentence executive digests, which I refine for accuracy and tone. |
| 8 | **Feature Importance & Error Analysis Breakdown** | **Collaborate with AI** | AI computes initial confusion matrix summaries, while I analyze false positives in domain context to find root causes. |
| 9 | **Automated Pipeline Log Parsing & Task Notification** | **Fully Automate** | Background scripts parse exit codes and send automated alerts without requiring active human intervention. |
| 10 | **Dataset Schema Validation & Data Contract Formatting** | **Fully Automate** | Schema type-checking and null-value bounds testing are rule-based operations best handled by automated scripts. |
| 11 | **HTML/CSS Research Paper UI Styling & Layout Generation** | **Delegate to AI with Review** | AI generates modern glassmorphism CSS and responsive flexbox layouts, which I test across screen sizes. |
| 12 | **GitHub Commit Message Formatting & PR Release Summaries** | **Delegate to AI with Review** | AI generates standardized Conventional Commit messages from diff logs, requiring a 5-second review before push. |

---

## 2. AI Toolkit & Academy Enrollment Evidence

### Tool Accounts Established
- **Claude (Anthropic)**: Configured with custom system prompts and Claude Project workspace.
- **ChatGPT (OpenAI)**: Active account setup for cross-model reasoning and secondary code reviews.
- **Anthropic Academy**: Enrolled in *AI Fluency: Framework & Foundations*.

### Anthropic Academy Certification Status
- **Course**: *AI Fluency: Framework & Foundations*
- **Module Completed**: Module 1 — *The AI Fluency Framework & Task Mapping*.
- **Key Takeaway**: Effective AI collaboration requires clear delegation boundaries: automating zero-variance tasks, delegating boilerplate with verification, collaborating on complex synthesis, and strictly protecting human-only judgment.

---

## 3. Claude Project Configuration

- **Project Name**: `FlyRank Search Intelligence & ML Engineering`
- **Project Purpose**: Centralized assistant workspace for data contract auditing, DuckDB optimization, and research paper drafting.

### Custom Instructions Configured

```text
Who I Am:
I am an ML Intern at FlyRank working on Applied Search Intelligence, dataset auditing, and Content Opportunity Scoring.

Tone & Style Preferences:
- Direct, clear, concise, and professional (no fluff or filler introductions).
- Ground all code solutions in empirical evidence and honest metrics (ROC-AUC, Precision@K).
- Strictly adhere to public safety rules: pseudonymize all client IDs, never generate fake causal claims, and use decision-support terminology.

Current Goals:
- Build robust, honest ML pipelines using DuckDB and scikit-learn.
- Maintain a clean git repository with automated test passing.
- Write clear research papers following canonical 9-section structures.
```

### Project Workspace Mockup / Visual Verification

```text
+-----------------------------------------------------------------------------------+
|  [Claude Project] FlyRank Search Intelligence & ML Engineering                   |
+-----------------------------------------------------------------------------------+
|  System Prompt: Loaded (Who I Am, Tone & Style, Public Safety Rules)              |
|  Knowledge Base:                                                                  |
|   - flyrank_data_schema.md                                                        |
|   - research_paper_canonical_template.md                                         |
|   - duckdb_parquet_query_guide.md                                                 |
|  Active Context Window: 200k tokens (Claude 3.5 Sonnet / Claude 3.7)               |
+-----------------------------------------------------------------------------------+
```

---

## 4. Target Tasks for FL-02 through FL-04 with "Done Well" Definitions

We select three specific tasks from the workflow audit table to refine across assignments FL-02, FL-03, and FL-04.

### Target Task 1: DuckDB SQL Query Construction & Parquet Aggregation
- **Workflow Category**: `Collaborate with AI` (FL-02 Focus)
- **Context**: Querying 9.8M-row Hugging Face Parquet slices using DuckDB without downloading full datasets locally.
- **What "Done Well" Means**:
  - The generated SQL query executes in under 5 seconds natively over `hf://` paths.
  - Zero data leakage: feature windows (March 1–15) and outcome windows (March 16–31) are strictly isolated with explicit `CASE WHEN` bounds.
  - Returns clean content-level aggregations (`imp_feat`, `clk_feat`, `pos_feat`, `content_age_days`) ready for pandas DataFrame ingestion.

### Target Task 2: Technical Research Summarization & Paper Drafting
- **Workflow Category**: `Delegate to AI with Review` (FL-03 Focus)
- **Context**: Converting executed notebook metrics into a public 9-section research paper (`docs/index.html` and `work/capstone_report.md`).
- **What "Done Well" Means**:
  - Includes all 9 canonical sections (Title + 5-sentence Abstract through Acknowledgments & Data Credit).
  - Contains honest claim framing (uses *observed*, *measured*, *directional*, *decision-support* language; zero false causal claims).
  - Data credit link to `https://flyrank.ai` is present, clickable, and verified by automated CI scripts.

### Target Task 3: Automated Dataset Contract Validation & Metric Logging
- **Workflow Category**: `Fully Automate` (FL-04 Focus)
- **Context**: Validating dataset grains, null bounds, leakage flags, and saving JSON metric receipts automatically.
- **What "Done Well" Means**:
  - Automated Python script checks schema types, null counts, date boundaries, and raises exit code `1` immediately if leaked target fields are detected.
  - Generates JSON summary receipts in `outputs/` without requiring manual human data inspection.
  - Integrates seamlessly into GitHub Actions CI workflows (`smoke-test.yml`).

---

## 5. Verification Checklist

- [x] 12 recurring tasks listed and classified with individual one-line rationales.
- [x] At least 2 tasks honestly marked as `Just Me` with non-delegable human rationale.
- [x] Tool accounts established (Claude, ChatGPT, Anthropic Academy) with Module 1 completion documented.
- [x] Claude Project custom instructions and system prompt defined.
- [x] Three target tasks selected with explicit, measurable "Done Well" success definitions.
