# Data dictionary and analysis levels

Files use UTF-8 CSV, comma delimiters, decimal points and no formulas. A missing entry is not always a negative finding.

- `SOURCE_INDEX.csv`: one row per published study (`study_id`, `doi`, `source_url`, published-endpoint count in archive). DOI is reference metadata, not a claim of source-content redistribution rights.
- `PAIRWISE_GATES.csv`: one row for each unordered pair of 24 sources (276 pairs). `PASS`, `FAIL` and `UNKNOWN` are **evidence-based screening dispositions**, not probabilistic scores. The six marginal gates need not pass jointly.
- `PAIRWISE_TOTALS.csv`: independently recalcable marginal totals for these gates; denom 276 per gate.
- `PRIORITY_PAIR_ADJUDICATION.csv`: focused follow-up of 15 pairs with a shared named particle-size statistic; statuses are task-specific.
- `PRIORITY_SOURCE_EVIDENCE.csv`: source-related citations and qualified feature observations for six high-priority studies.
- `STAGE_COUNTS.csv`: stage disposition categories. `Stage review unresolved` is not equivalent to `not reported by original authors`. Derived endpoints have no one-to-one measurement-age interpretation.
- `ENDPOINT_GROUP_COUNTS.csv`: summary counts by endpoint statistic/class; categories overlap across studies but records are not duplicated within a class.
- `REPEAT_GROUP_SUMMARY.csv`: one row per published same-coordinate group, **not a transferable experimental error parameter**. `cv_percent` and `range_nm` are derived from previously transcribed published run means. The actual run identifiers and measurements have been withheld in this candidate.
- `REPEAT_SENSITIVITY.csv`: five reported group filters: all, published design-centre repeats, other run IDs, excluding Wan Ishak, excluding identical printed means.
- `FROZEN_RECALCULATED.csv`: six models × (NEW001, NEW008, pooled). `unique_predictions=1` and `prediction_span_nm=0` within every heldout source; pooled rows may contain two distinct fitted source-level constants. The MAE values are archived computations, not model refits performed by public scripts.
