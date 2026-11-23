#!/usr/bin/env python3
"""Recompute selected released aggregate results (Python 3 standard library only).

No historical model fitting is performed. No unapproved third-party tables are required.
"""
from __future__ import annotations
import csv, json, math, statistics, pathlib, collections

BASE=pathlib.Path(__file__).resolve().parents[1]
DATA=BASE/'data'/'derived'
OUT=BASE/'outputs'


def read(name):
    with (DATA/name).open(encoding='utf-8-sig',newline='') as h:
        return list(csv.DictReader(h))

def write(path, rows):
    with path.open('w',encoding='utf-8',newline='') as h:
        w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)

def approximately(x,y,tolerance=1e-8):
    return math.isclose(float(x),float(y),abs_tol=tolerance,rel_tol=1e-9)

def run():
    OUT.mkdir(exist_ok=True)
    pairs=read('PAIRWISE_GATES.csv')
    assert len(pairs)==276, f'Expected 276, found {len(pairs)}'
    gates=['numeric_size','statistic','stage','shared_input','input_variation','train_test_support']
    recomputed=[]
    for gate in gates:
        counts=collections.Counter(r[gate] for r in pairs)
        assert set(counts)<= {'PASS','FAIL','UNKNOWN'}
        recomputed.append(dict(gate=gate,denominator=len(pairs),**{s:counts[s] for s in ('PASS','FAIL','UNKNOWN')}))
    archive_totals={r['gate']:r for r in read('PAIRWISE_TOTALS.csv')}
    for r in recomputed:
        a=archive_totals[r['gate']]
        for k in ('denominator','PASS','FAIL','UNKNOWN'):
            assert int(a[k])==r[k],(r['gate'],k,r[k],a[k])
    write(OUT/'reproduced_pairwise_totals.csv',recomputed)

    groups=read('REPEAT_GROUP_SUMMARY.csv')
    assert len(groups)==32
    assert len({r['group_id'] for r in groups})==32
    subsets={
        'all': groups,
        'reported_design_centers':[r for r in groups if r['replicate_layer'].startswith('Published')],
        'other_run_ids':[r for r in groups if not r['replicate_layer'].startswith('Published')],
        'exclude_Wan_Ishak':[r for r in groups if r['study_id']!='P5S10'],
        'exclude_identical_reported_means':[r for r in groups if not r['rounding_flag']],
    }
    sensitivity=[]
    for label,rows in subsets.items():
        cv=[float(r['cv_percent']) for r in rows]
        ranges=[float(r['range_nm']) for r in rows]
        sensitivity.append(dict(subset=label,groups=len(rows),studies=len({r['study_id'] for r in rows}),
            cv_min=min(cv),cv_median=statistics.median(cv),cv_max=max(cv),
            range_min=min(ranges),range_median=statistics.median(ranges),range_max=max(ranges),
            cv_above_20=sum(x>20 for x in cv)))
    expected={r['subset']:r for r in read('REPEAT_SENSITIVITY.csv')}
    for row in sensitivity:
        exp=expected[row['subset']]
        for k,v in row.items():
            if k=='subset':continue
            assert approximately(v,exp[k]), (row['subset'],k,v,exp[k])
    write(OUT/'reproduced_repeat_sensitivity.csv',sensitivity)

    with (BASE/'data'/'provenance'/'SOURCE_INDEX.csv').open(encoding='utf-8-sig', newline='') as h:
        source=list(csv.DictReader(h))
    assert len(source)==24
    assert len({r['study_id'] for r in source})==24
    assert sum(int(r['endpoint_records_in_curated_archive']) for r in source)==1159
    assert all(r['source_url'].startswith('https://doi.org/10.') for r in source)

    stage=read('STAGE_COUNTS.csv')
    assert sum(int(r['n']) for r in stage)==1159
    unresolved=sum(int(r['n']) for r in stage if r['stage_status']=='Stage review unresolved')
    assert unresolved==459
    priority=read('PRIORITY_PAIR_ADJUDICATION.csv')
    assert len(priority)==15

    frozen=read('FROZEN_RECALCULATED.csv')
    assert len(frozen)==18
    assert len({r['model'] for r in frozen})==6
    within=[r for r in frozen if r['fold']!='Pooled']
    assert len(within)==12
    assert all(int(r['unique_predictions'])==1 and approximately(r['prediction_span_nm'],0.0) for r in within)
    assert {int(r['n']) for r in within}=={9,10}
    lookup={(r['model'],r['fold']):r for r in frozen}
    mae_rf=float(lookup['random_forest','Pooled']['mae'])
    mae_mean=float(lookup['train_mean','Pooled']['mae'])
    assert approximately(mae_rf,40.944612050960714) and approximately(mae_mean,45.70857699805068)
    summary={
        'study_count':len(source),'endpoint_records':1159,'screened_study_pairs':len(pairs),
        'screened_pairs_with_confirmed_statistic_match':next(r['PASS'] for r in recomputed if r['gate']=='statistic'),
        'priority_pairs_reviewed':len(priority), 'repeat_groups':len(groups),
        'repeat_cv_median_percent':next(r['cv_median'] for r in sensitivity if r['subset']=='all'),
        'repeat_cv_median_excluding_Wan_Ishak_percent':next(r['cv_median'] for r in sensitivity if r['subset']=='exclude_Wan_Ishak'),
        'stage_unresolved_records':unresolved,
        'frozen_oof_predictions_from_archived_metadata':114, 'frozen_fitted_groups_with_zero_span':len(within),
        'pooled_rf_mae_nm_archived':mae_rf,'pooled_train_mean_mae_nm_archived':mae_mean,
        'delta_mae_mean_minus_rf_nm':mae_mean-mae_rf,
        'model_refit_status':'MODEL_REFIT_NOT_REPRODUCED',
        'frozen_oof_metrics_status':'SUMMARY_CONSISTENCY_CHECK_ONLY',
    }
    (OUT/'report.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2,ensure_ascii=False))
    return summary

if __name__=='__main__':
    run()
