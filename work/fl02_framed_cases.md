# Voice Card & Framed Case Studies (FL-02)

- **Author:** Rida Eman (Computer Science Undergraduate & ML Intern at FlyRank AI)
- **Track:** AI Fluency Track (Frame It as Cases)
- **Repo:** [github.com/ridaeman02/flyrank-ml-internship](https://github.com/ridaeman02/flyrank-ml-internship)
- **Date:** 2026-09-18

---

## 1. Voice Card (Standing Instruction)

```text
Voice Card: Direct, plainspoken, honest, technical, zero buzzwords.
```

### Standing Instruction for Claude Project:
> "Write like a real software and machine learning engineer. Be direct, concise, and plainspoken. Never use buzzwords or filler like 'spearheaded', 'game-changer', 'results-driven', 'delve', or 'seamless'. State what was built, the concrete decisions made, and the exact numbers without inflating them. Always use active voice."

---

## 2. Before & After: Generic AI Copy vs. My Edited Version

| Version | Copy | Why It Changed |
|---|---|---|
| **Before (Generic AI)** | *"I spearheaded an innovative, cutting-edge machine learning solution leveraging state-of-the-art predictive algorithms on massive big data to seamlessly revolutionize organic search optimization and drive unparalleled traffic growth."* | Puffed up with meaningless buzzwords ('spearheaded', 'cutting-edge', 'leveraging', 'seamlessly', 'unparalleled'). It hides what the model actually does and makes unverifiable claims. |
| **After (My Edited Voice)** | *"I built a logistic regression pipeline in DuckDB and scikit-learn that scores decaying search pages across 9.8 million daily rows. Evaluated on unseen client domains, it reached 0.5000 Precision@50, beating FlyRank's fixed heuristic baseline of 0.4200."* | Direct, grounded, and specific. Names the exact tools, dataset size, split design, and empirical test result. |

---

## 3. Framed Case Study 1 (Lead Project): Content Refresh Opportunity Scoring

### Beat 1: The Problem
SEO teams manage thousands of published articles. Over time, search traffic decays, but identifying which pages need a rewrite is usually done with blunt rules (e.g., "any page older than 6 months"). Editorial teams waste hours rewriting pages that would have recovered on their own or miss dying high-traffic pages until it is too late. They needed a model to rank pages by likelihood of continued decline so writers work on high-impact articles first.

### Beat 2: What I Did & Decided
- **Data Grain & Slicing**: Queried 9,841,378 daily performance rows from the FlyRank warehouse using DuckDB, aggregating to the content-page grain for March 2026.
- **Strict Leakage Prevention**: Kept the feature window (March 1–15) strictly separate from the outcome window (March 16–31). Intentionally tested a "leakage trap" using target-derived metrics (`trend_pct`), showing how leakage artificially inflates ROC-AUC to 0.9991 before stripping it out.
- **Client Normalization**: Discovered that absolute traffic numbers caused models to memorize large client traffic rather than learning page decay patterns. Standardized impressions and clicks within each client (`imp_norm`, `clk_norm`).
- **Honest Split Choice**: Rejected a standard random train/test split (which showed an inflated 0.7319 ROC-AUC). Evaluated models using a `GroupShuffleSplit` on `client_hash_id` (75% train, 25% test) to test whether predictions hold up on client domains the model has never seen.

### Beat 3: What Came of It
- On the unseen client holdout set, the baseline heuristic achieved **0.4200 Precision@50**.
- The normalized Logistic Regression model achieved **0.5000 Precision@50** (a 19% relative precision gain).
- Generated a prioritized Action Playbook of 30,000 scored candidate pages with transparent reason codes (`stale_visible_page`, `low_ctr_visible_page`, `model_decline_risk`) so human editors understand why a page was recommended.
- Published and deployed the research paper live at `https://ridaeman02.github.io/flyrank-ml-internship/`.

---

## 4. Framed Case Study 2 (Supporting Piece): Leakage-Free Temporal ETL & Contract Verification

### Beat 1: The Problem
In production time-series and search data, data contracts are rarely validated before training. Future observations quietly leak into training features, resulting in models that look brilliant in notebooks but fail immediately in production.

### Beat 2: What I Did & Decided
- Built an automated pre-flight assertion suite in Python (`scripts/verify_data_contract.py`).
- Implemented deterministic checks that block execution if future dates appear in the feature window or if forbidden columns (`trend_direction`, `trend_pct`, `priority_score`) enter the feature matrix.
- Added automated null checks and base rate comparison assertions that output a persistent JSON receipt (`outputs/verification_receipt.json`).

### Beat 3: What Came of It
- Shrunk verification time from 20 minutes of manual inspection to under 1.2 seconds.
- Integrated directly into GitHub Actions CI (`smoke-test.yml`), guaranteeing that any code introducing leakage or missing outputs fails the build before merge.

---

## 5. Bio & Contact / CTA Copy

### Bio (About Me)
I am a Computer Science undergraduate and Machine Learning Intern at FlyRank AI. I work on backend pipelines (Python, DuckDB, SQL) and applied search ranking models. My focus is building models that work on messy real data and holding myself to honest validation standards—no inflated claims, no data leakage, and no black-box scores without reason codes.

### Contact / Call to Action (The One Action)
If you are a Lead Data Scientist or ML Engineering Manager looking for someone who writes clean, honest code and understands production data pipelines:

- **The Action**: [Invite me for a technical interview](mailto:ridaeman0002@gmail.com)
- **GitHub**: [github.com/ridaeman02/flyrank-ml-internship](https://github.com/ridaeman02/flyrank-ml-internship)
- **Deployed Research Paper**: [ridaeman02.github.io/flyrank-ml-internship](https://ridaeman02.github.io/flyrank-ml-internship/)
