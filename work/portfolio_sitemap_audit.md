# AI Fluency — Portfolio Sitemap Sketch & Pressure-Test Audit

- **Author:** Rida Eman (Computer Science Undergraduate & ML Intern at FlyRank AI)
- **Track:** AI Fluency Track (Portfolio & Proof Path)
- **Repo:** [github.com/ridaeman02/flyrank-ml-internship](https://github.com/ridaeman02/flyrank-ml-internship)
- **Date:** 2026-08-07

---

## 1. Portfolio Sitemap & User Path Sketch

The portfolio path is intentionally lean (4 core sections/pages max) to guide a technical hiring manager or research lead from initial impression to decision action without unnecessary friction.

```text
+-----------------------------------------------------------------------------------+
|                            PORTFOLIO SITEMAP FLOW                                 |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  [PAGE 1: HERO / LANDING]                                                         |
|   ├── Bold Headline Claim: "Building Honest ML Systems & Applied Search Intelligence" |
|   ├── Proof Teaser: 9.8M-row search warehouse model & 0.5000 Precision@50 lift    |
|   └── Primary CTA: "View Research Paper & Capstone" (Scrolls to Work)             |
|                                                                                   |
|                                     │                                             |
|                                     ▼                                             |
|  [PAGE 2: WORK / CASE STUDIES (THE PROOF)]                                        |
|   ├── Capstone Research Paper: Content Refresh Opportunity Scoring & Ranking     |
|   ├── Interactive Metric Cards: Precision@50 (0.5000) vs Baseline (0.4200)         |
|   ├── Methodology Receipts: Client-Holdout Split & DuckDB SQL Pipeline           |
|   └── Direct Links: GitHub Repository & Live Deployed Research Paper              |
|                                                                                   |
|                                     │                                             |
|                                     ▼                                             |
|  [PAGE 3: ABOUT & METHODOLOGY]                                                    |
|   ├── Profile: CS Senior & ML Intern at FlyRank AI (Python, Django, MLOps)        |
|   ├── Engineering Principles: Core First, AI Second & Zero Data Leakage Rules     |
|   └── Tooling & Stack: scikit-learn, DuckDB, Hugging Face, GitHub Actions CI      |
|                                                                                   |
|                                     │                                             |
|                                     ▼                                             |
|  [PAGE 4: CONTACT & ONE ACTION]                                                   |
|   ├── The One Action: Direct Scheduling / Contact Form for ML Roles               |
|   └── Social Proof: GitHub, LinkedIn, & Live Deployed Paper Link                  |
|                                                                                   |
+-----------------------------------------------------------------------------------+
```

### Page Purpose & Justification Table

| Page / Section | Core Purpose | Earned Place Rationale | Target Action Supported |
|---|---|---|---|
| **1. Hero / Landing** | State the central claim immediately. | Hook the visitor in 5 seconds with a quantitative proof headline. | Drives visitor to inspect the empirical work below. |
| **2. Work / Case Studies** | Prove the claim with real evidence. | Essential proof element; showcases the 9.8M-row warehouse pipeline and live deployed paper. | Establishes technical credibility and model performance. |
| **3. About / Method** | Establish trust and identity. | Answers "who built this and how do they think?" — details public safety & honest split philosophy. | Demonstrates engineering maturity and rigor. |
| **4. Contact / Action** | Enable immediate conversion. | Removes all friction between reading the paper and scheduling an interview. | **The One Action**: Contact / Hire / Collaborate. |

---

## 2. Tool Accounts & AI Tutor Project Setup

### Toolkit Status
- **Claude (Anthropic)**: Configured with dedicated Claude Project (`FlyRank ML Portfolio & Research Showcase`) acting as a technical tutor.
- **ChatGPT (OpenAI)**: Active account for cross-validation.
- **Gemini (Google)**: Active account for data pipeline critique.
- **Perplexity AI**: Active account for research paper citations and benchmarking.

### Configured Claude Project Instructions (Tutor Mode)

```text
Project Name: FlyRank ML Portfolio & Research Showcase
Role: AI Tutor & Senior ML Engineering Mentor

System Instructions:
Who I am: I am Rida Eman, a Computer Science undergraduate student and Machine Learning Intern at FlyRank AI working on backend data pipelines (Python, Django, DuckDB) and serverless MLOps.

My Core Claim & Proof Statement:
"I build honest, production-grade Machine Learning pipelines for search intelligence. In my capstone project on a 9.8M-row search warehouse dataset, my client-normalized Logistic Regression model achieved a 0.5000 Precision@50 score (a 19% relative lift over standard heuristic rules) evaluated on a strict client-holdout split."

Your Role as Tutor:
- Act as an empathetic, rigorous Senior ML Engineering Mentor and Technical Portfolio Tutor.
- Help me pressure-test my portfolio sitemap, user flows, and technical writing.
- Be direct, clear, and concise. Never use fluff or jargon words like 'delve', 'robust', 'seamless', or 'leverage'.
- Enforce public safety rules: pseudonymize all data, require evidence for claims, and emphasize decision-support terminology.
```

---

## 3. Real Pressure-Test Prompt & Output

### The Pressure-Test Prompt

```text
"Tutor, please pressure-test my proposed 4-page portfolio sitemap against my central claim ('I build honest, production-grade ML pipelines for search intelligence with a 0.5000 Precision@50 score on 9.8M rows') and my One Action ('Schedule an ML engineering interview / contact me'). 

Critique the flow from landing to conversion. Are there any unnecessary pages, weak proof points, or friction bottlenecks in the user journey?"
```

### Claude Project Pressure-Test Response (Saved Output)

```text
Got it — let's pressure-test your 4-page portfolio map against your core claim and single conversion goal.

1. What Works Well:
- Direct Alignment: Page 2 (The Work) directly backs up your headline claim with real numbers (0.5000 Precision@50 vs 0.4200 baseline).
- Lean Structure: Keeping it to 4 pages avoids fluff and respects a hiring manager's limited time.

2. Critical Bottlenecks & Friction Points:
- Friction Point #1: Requiring a visitor to navigate to Page 4 just to take the 'One Action' adds an unnecessary click. Technical recruiters often read case studies and want to reach out immediately without jumping pages.
- Friction Point #2: The 'About' page risks separating your personality from your technical proof if treated as a standalone bio.

3. Recommended Sitemap Refinement:
- Merge Action Into Every Footer: Keep the contact form and social proof sticky in the footer of every page so the visitor can act the moment they are convinced.
- Integrate Method into Work: Move your engineering principles (Core First, Honest Splits) directly alongside the Capstone Case Study rather than isolating them on a separate bio page.
```

---

## 4. Key Sitemap Refinements Based on Pressure Test

Based on the pressure-test feedback from Claude, I am making **two concrete refinements** to the portfolio layout:

1. **Embedded Action Footer**: Instead of forcing visitors to navigate to a separate `Contact` page, I embedded the primary action (Contact / LinkedIn / GitHub links) into a persistent footer across all pages.
2. **Methodology & Proof Pairing**: I integrated the engineering principles (client-holdout split design, zero leakage rules) directly into the Capstone Work section so that technical credentials and proof are presented together.

---

## 5. Visual Proof & Screenshot Evidence

- **Screenshot Saved**: Embedded in PDF at `work/figures/claude_screenshot.png` and `docs/img/claude_screenshot.png`.
- **PDF Deliverables Generated**:
  - [work/portfolio_sitemap_audit.pdf](file:///c:/Users/Rida%20Eman/Downloads/Flyrank%20AI_intenship/work/portfolio_sitemap_audit.pdf)
  - [submission/portfolio_sitemap_audit.pdf](file:///c:/Users/Rida%20Eman/Downloads/Flyrank%20AI_intenship/submission/portfolio_sitemap_audit.pdf)

---

## 6. Verification Checklist

- [x] Sitemap sketch is lean (4 sections max) and every page earns its place against the claim and action.
- [x] Claude Project configured with genuine custom instructions and tutor role.
- [x] First prompt pressure-tested the map against claim and action, with outputs saved.
- [x] At least one concrete sitemap refinement documented based on pressure-test feedback.
- [x] PDF submission generated and committed to repo.
