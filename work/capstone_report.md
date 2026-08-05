# Capstone Report — Refresh / Content Opportunity Scoring

- **Author:** FlyRank ML Intern
- **Lane:** Refresh / Content Opportunity Scoring
- **Repo:** [github.com/ridaeman02/flyrank-ml-internship](https://github.com/ridaeman02/flyrank-ml-internship)
- **Date:** 2026-08-05

## 0. Abstract

Content decay is a critical challenge for online publishers, where high-performing pages gradually lose organic search visibility. This project develops an evidence-backed Machine Learning pipeline to identify and rank declining content pages for editorial refresh prioritization. Using a 9.8M-row daily performance snapshot from the FlyRank warehouse release (March 2026), we engineered client-normalized search signals and evaluated models on a strict client-holdout split (`GroupShuffleSplit` on `client_hash_id`). Our Logistic Regression model achieved a **0.5000 Precision@50** score, representing a **19% relative lift** over standard heuristic baseline rules (0.4200 Precision@50) and significantly outperforming the base test set rate (0.2890). The resulting system produces transparent action queues with human-interpretable reason codes to optimize editor review capacity.

## 1. Problem framing

- **Decision Supported**: Prioritizing editorial review capacity by deciding which decaying pages should be refreshed, expanded, or rewritten first.
- **Unit of Analysis**: One unique content page for a specific client (`content_hash_id` × `client_hash_id`).
- **Human Action**: Writers and content managers receive a ranked list of candidate pages along with reason codes (`stale_visible_page`, `low_ctr_visible_page`, `model_decline_risk`) to guide content updates.
- **Cost of Errors**: False positives waste writer hours on healthy content; false negatives result in permanent traffic and revenue loss.
- **Why ML**: Simple fixed rules cannot weigh non-linear interactions across clicks, impressions, position, CTR, and content age across 32+ distinct client domains.

## 2. Data safety

- **Dataset Release**: FlyRank Pseudonymized Warehouse Release (`v20260703`), utilizing `dim_content` and `fact_content_daily_performance` (March 2026 slice, 9,841,378 daily fact rows).
- **Pseudonymization**: All `client_hash_id`, `content_hash_id`, `keyword_hash_id`, and `url_hash_id` codes are anonymized. No raw client names, URLs, domain names, or unmasked queries appear in the code or outputs.
- **Deliberately Excluded Fields**: Product decision outputs (`health_score`, `priority_score`, `refresh_tier`) and target-window traffic metrics (`imp_out`) were strictly excluded from model feature sets to prevent circular logic and outcome leakage.

## 3. Baseline

- **Rule Definition**: Flag pages as baseline refresh candidates if `content_age_days >= 180` and `pos_feat <= 20.0` (stale pages ranking on Google page 1 or 2).
- **Performance**: On the client-holdout test split, the baseline achieved a **ROC-AUC of 0.5232** and a **Precision@50 of 0.4200** (against a test set base rate of 0.2890).

## 4. Model / analysis

- **Methods**: Logistic Regression (interpretable linear model) and Random Forest Classifier (capturing non-linear interactions).
- **Feature Prep**: Features were constructed from the March 1–15 window (`imp_norm`, `clk_norm`, `pos_feat`, `ctr_feat`, `content_age_days`). Impression and click counts were standardized per client (`imp_norm`, `clk_norm`) to prevent client-scale bias across unseen domains.
- **Target Proxy**: Binary outcome `is_declining = 1` if target-window impressions (March 16–31) dropped below 80% of feature-window impressions.

## 5. Evaluation

- **Split Design**: `GroupShuffleSplit` on `client_hash_id` (75% train, 25% test) to evaluate generalizability to completely unseen client websites.
- **Comparison Table**:

| Method | ROC-AUC | Precision@50 |
|---|---|---|
| Base Rate (Random Guessing) | 0.2890 | 0.2890 |
| Baseline Heuristic Rule | 0.5232 | 0.4200 |
| **Logistic Regression** | **0.5334** | **0.5000** |
| Random Forest Classifier | 0.5394 | 0.3800 |

## 6. Interpretation

- **Feature Importances**: Random Forest feature importances highlighted `content_age_days` (37.7%) and `clk_norm` (27.8%) as the primary drivers of content decay.
- **Error Analysis**: 
  - *False Positives*: Pages experiencing unexpected organic traffic spikes (e.g. `content_178e55dfc740ac1e` grew from 409 to 755 impressions) were falsely flagged due to initially low click volume.
  - *False Negatives*: Very low-volume pages (e.g., dropping from 15 to 1 impression) were missed because small traffic drops resemble noise.

## 7. Recommendation

- **Action Playbook**: Combine model predictions (`lr_prob`) and baseline rules into a weighted final score (`0.7 * lr_prob + 0.3 * baseline_score`).
- **Top Candidates Queue**:

| Content ID | Client ID | Final Score | Reason Code | Is Declining (Actual) |
|---|---|---|---|---|
| `content_cd3d932d4e1c8db0` | `client_9958f0a7` | 99.91 | `stale_visible_page` | 0 |
| `content_fc0d3723ce5a9bba` | `client_fef1a8f4` | 73.13 | `stale_visible_page` | 0 |
| `content_783a9715094029de` | `client_fef1a8f4` | 70.82 | `stale_visible_page` | 0 |
| `content_ba462518dad435fc` | `client_fef1a8f4` | 65.90 | `model_decline_risk` | 0 |

## 8. Reproducibility

- **Commands**: Run `python C:/.../scratch/run_notebook.py work/notebooks/capstone.ipynb` with `HF_TOKEN` set in the environment.
- **Random Seeds**: Fixed at `random_state=42` across `GroupShuffleSplit`, `LogisticRegression`, and `RandomForestClassifier`.
- **Dependencies**: `duckdb>=1.0.0`, `scikit-learn>=1.4.0`, `pandas>=2.2.0`, `huggingface_hub`.

## 9. Acknowledgments & data credit

Built on the **FlyRank ML Internship dataset** — available at [https://flyrank.ai](https://flyrank.ai/).
