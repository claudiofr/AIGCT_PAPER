import pandas as pd
from table_renderer import TableRenderer

from aigct.container import VEBenchmarkContainer


def render_label_stats(query_mgr, table_renderer):
    label_stats = query_mgr.get_all_task_variant_effect_label_stats()
    score_stats = query_mgr.get_all_variant_effect_source_stats()
    label_stats = label_stats.merge(score_stats, on=["TASK_CODE"], how="inner")
    label_stats = label_stats[["TASK_CODE", "NUM_VARIANTS",
                               "NUM_POSITIVE_LABELS", "NUM_NEGATIVE_LABELS",
                               "NUM_GENES", "NUM_SCORE_SOURCES"]]
    label_stats["TASK_CODE"] = label_stats["TASK_CODE"].apply(
        lambda code: "ClinVar" if code == "CLINVAR" else
        "Cancer" if code == "CANCER" else code)
    table_renderer.render_label_stats(label_stats, "label_stats.html")


container = VEBenchmarkContainer("config/aigct.yaml")
table_renderer = TableRenderer("out")

query_mgr = container.query_mgr

render_label_stats(query_mgr, table_renderer)
