<DOMAIN_KNOWLEDGE>
  <DATASET_SCHEMA>
    - fact_content_daily_performance: report_date, client_hash_id, content_hash_id, gsc_impressions, gsc_clicks, gsc_avg_position
    - dim_content: content_hash_id, content_created_date, word_count, primary_keyword
    - Grain: One row per content page per client per day (March 2026 slice: 9,841,378 rows).
  </DATASET_SCHEMA>
  
  <PUBLIC_SAFETY_RULES>
    - Never include real client names, unmasked URLs, credentials, or raw query text.
    - All IDs must remain pseudonymized (client_hash_id, content_hash_id).
    - Always link data credit to https://flyrank.ai ("Built on the FlyRank ML Internship dataset").
  </PUBLIC_SAFETY_RULES>

  <CANONICAL_PAPER_STRUCTURE>
    1. Title + Abstract (5 sentences: question -> data -> method -> headline result -> output use)
    2. Introduction / Problem (decision support for content refresh)
    3. Data (tables, date windows, exclusions)
    4. Methodology (is_declining label, GroupShuffleSplit on client_hash_id, baseline rule)
    5. Results (Model vs Baseline table: Precision@50 = 0.5000 vs Baseline = 0.4200)
    6. Limitations & Honest Framing (observational, non-causal, 15-day window noise)
    7. Ranked Recommendations (reason codes: stale_visible_page, low_ctr_visible_page, model_decline_risk)
    8. Reproducibility (notebook links, seeds, environment)
    9. Acknowledgments & Data Credit (link to https://flyrank.ai)
  </CANONICAL_PAPER_STRUCTURE>
</DOMAIN_KNOWLEDGE>
