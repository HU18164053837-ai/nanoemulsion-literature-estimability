import pathlib
import sys
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from reproduce_public import run

class AggregateReproductionTest(unittest.TestCase):
    def test_summary(self):
        result=run()
        self.assertEqual(result['study_count'],24)
        self.assertEqual(result['screened_study_pairs'],276)
        self.assertEqual(result['stage_unresolved_records'],459)
        self.assertEqual(result['frozen_fitted_groups_with_zero_span'],12)
        self.assertLess(result['pooled_rf_mae_nm_archived'],result['pooled_train_mean_mae_nm_archived'])

if __name__=='__main__': unittest.main()
