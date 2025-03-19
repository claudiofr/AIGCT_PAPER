import context  # noqa: F401
import pytest
aigctp.paper import
from aigct.model import VEQueryCriteria
from aigct.query import VEBenchmarkQueryMgr
from aigct.reporter import VEAnalysisReporter
from aigct.pd_util import filter_dataframe_by_list

# from aigct.model import VariantId  # noqa: F401

test_tasks = ["CANCER", "CLINVAR", "DDD", "CHD", "ASD", "ADRD" ]
# test_tasks = ["CLINVAR" ]


# @pytest.mark.parametrize("task_code", test_tasks)
def test_compute_metrics_basic(ve_analyzer,
                               sample_user_scores):
    task_cd = sample_user_scores[0]
    metrics = ve_analyzer.compute_metrics(
        task_cd, list_variants=True)
    pass
