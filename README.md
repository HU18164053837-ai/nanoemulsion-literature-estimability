# Literature-derived nanoemulsion data: compatibility and model estimability

This analysis release accompanies a manuscript prepared for *Journal of Chemometrics*. It examines measurement compatibility, dispersion among published runs at matched formulation coordinates and the behavior of frozen leave-one-study-out predictions.

## Study scale

| Unit | N |
|---|---:|
| Independent published studies | 24 |
| Formulation coordinates | 424 |
| Published experimental runs | 513 |
| Endpoint records | 1,159 |
| Within-coordinate published-run groups | 32 |
| Unordered study pairs screened | 276 |
| Frozen source-held-out model predictions | 114 (six methods; 19 formulations; two held-out sources) |

These units are not interchangeable. The 24-study database **was not used as a 24-study cross-source machine-learning training cohort**. The source-held-out model diagnosis uses only NEW001 and NEW008. Within each test source the archived prediction was constant for every method; the observed pooled random-forest MAE gain does **not** establish formulation-level discrimination.

## Directory map

- `data/derived/`: **author-computed summary and adjudication tables**, with no publisher PDF, HTML cache, full per-run extraction, or confidential replay archive.
- `data/provenance/SOURCE_INDEX.csv`: study identifiers, DOI references and record counts, with redistribution status marked as not reviewed.
- `scripts/reproduce_public.py`: Python 3 **standard-library-only** re-computation of the aggregate pairwise gate counts and run-group sensitivity summaries, plus internal-consistency checks of frozen model-summary metrics. It does not refit a model.
- `figures/`: original Phase 6 figure previews, retained unchanged.
- `docs/`: data definitions, provenance, permitted scope and release checklist.
- `tests/`: automated checks.

## Reproduction

```bash
python scripts/reproduce_public.py
python -m unittest discover -s tests -v
```

The first command generates `outputs/report.json` and `outputs/reproduced_pairwise_totals.csv` / `outputs/reproduced_repeat_sensitivity.csv`. Standard Python 3 is sufficient. The archived **114 row-level predictions and observations are not included** in this initial public package pending source-by-source data-rights verification. Thus the code **checks** the released frozen summary but does not independently recompute its MAE from original observations. Full model refitting was not independently reproduced (`MODEL_REFIT_NOT_REPRODUCED`). See `docs/REPRODUCIBILITY.md`.

## Data and interpretation safeguards

- `UNKNOWN` is *not* `FAIL` and must not be recoded as confirmed incompatibility.
- 459 records await manual review of exact measurement stage; this is not evidence that the published articles failed to report the stage.
- NEW008's exact measurement age for the frozen Table 4 responses is unresolved.
- The 32 matched-coordinate groups describe spread among **published run means**; the independent-preparation status may differ between sources.
- The 15 priority source pairs include one archived-input `NOT_ESTIMABLE` case, one conditional process candidate, and 13 with unresolved evidence.
- Source-level counts, per-run records, and model refit capability must not be conflated.

## Citation and status

This is a pre-submission research package. The manuscript is not presented as published or accepted; no journal DOI or repository DOI has been assigned. Authors: Yi Hu, Jiayao Li and Yiheng Jia. See `CITATION.cff`.

See `LICENSE` and `docs/RIGHTS_AND_RELEASE.md` for the release scope. Row-level OOF error re-computation and figure regeneration are ARCHIVED_RESULT_NOT_FULLY_REPRODUCIBLE_FROM_PUBLIC_FILES.
