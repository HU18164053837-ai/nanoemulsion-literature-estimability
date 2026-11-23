# Reproducibility and analysis boundary

This public package supports independent checks of the published aggregate evidence, not complete reconstruction of every historical modelling stage.

| Claim | Public inputs | Public script status | Limitation |
|---|---|---|---|
| 24-study / 1,159-endpoint provenance | `SOURCE_INDEX.csv` | Assert counts | Source-record extraction not included |
| 276 source-pair gate decisions | `PAIRWISE_GATES.csv` | Recompute six pass/fail/unknown totals | Eligibility decisions in archive, not independently re-adjudicated against all papers |
| 32 repeated-coordinate groups | `REPEAT_GROUP_SUMMARY.csv` | Recompute sensitivity summaries | Original run-level values excluded pending rights review |
| Measurement-stage disposition | `STAGE_COUNTS.csv` | Sum to 1,159 and flag 459 unresolved | Underlying source-stage evidence not re-reviewed |
| Frozen two-source OOF model comparison | `FROZEN_RECALCULATED.csv` | Validate all 12 within-fold prediction spans and reported summary values | 114 prediction rows not included; cannot independently recompute MAE or refit models |
| Figure 1/2/3 | `figures/` | Supplied output previews only | Exact figures not regenerated from these public aggregate inputs |

`MODEL_REFIT_NOT_REPRODUCED` is the status for historic model refitting. Do not describe these aggregate checks as successful independent retraining.

For the corresponding complete analysis reproduction, source-extracted per-run records, archived frozen prediction rows, source-specific feature/denominator decisions and the original figure code must be reviewed and lawfully released first. These material are excluded rather than silently marked as public.
