import os
import time

# self defined functions
from export_git.code.metric_collector.metric_collector import read_metrics
from export_git.code.user_input.filter import filter_dataframes
from export_git.code.decision_model.comparable_metrics import comparable_metrics
from export_git.code.decision_model.score_calculation import score_calculation
from export_git.code.decision_model.decision import decision


def watcher(old_conditions, weights):
    """
    DEFINE VARIABLES
    """
    metrics_static = ["withdrawal_time", "secure_transaction", "reputation"]
    l2_names = ["opti", "zk", "next", "poly"]

    thresholds = {'tps': [1.01, 5, 10, 29.9],
                  'withdrawal_time': [60, 10, 1, 0.1],
                  'secure_transaction': [60, 12, 5, 1],
                  "fee": [0.01, 0.09, 0.5, 2],
                  'reputation': [2, 3, 4, 5]}
    current_dir = os.path.dirname(os.path.dirname(__file__))
    static_path = os.path.join(current_dir, 'data')
    i = 2
    while(True):
        time.sleep(10)
        dynamic_path = os.path.join(current_dir, 'data', "dynamic_data", f"sample_{i}")
        if not os.path.exists(dynamic_path):
            break
        print("NOTE: The watcher activates, dynamic variables are calculated again.")

        f_df = read_metrics(static_path, dynamic_path, l2_names)

        f_df, old_conditions = filter_dataframes(f_df, rerun= 1, old_condition= old_conditions)

        comp_df = comparable_metrics(f_df, thresholds)

        metrics = list(thresholds.keys())
        score = score_calculation(comp_df, metrics, weights)
        x = decision(score, f_df, weights, metrics)

        i = i + 1
    print("Watcher finished work, no data exists anymore to analyse.")
    return 0