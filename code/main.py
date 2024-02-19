# AUTHOR: Tim Müller
# Date: 18.02.2024

# community packages
import os

# self define packages
from export_git.code.metric_collector.metric_collector import read_metrics
from export_git.code.user_input.filter import filter_dataframes
from export_git.code.user_input.weight import metric_weight
from export_git.code.decision_model.comparable_metrics import comparable_metrics
from export_git.code.decision_model.score_calculation import score_calculation
from export_git.code.decision_model.decision import decision
from watcher import watcher

"""
DEFINE VARIABLES
"""
current_dir = os.path.dirname(os.path.dirname(__file__))
static_path = os.path.join(current_dir, 'data')
dynamic_path = os.path.join(current_dir, 'data', "dynamic_data","sample_1")


#static_path = r"D:\TUHH\Thesis\export_git\data"
#dynamic_path = r"D:\TUHH\Thesis\export_git\data\dynamic_data\sample_1"
metrics_static = ["withdrawal_time", "secure_transaction", "reputation"]
l2_names = ["opti", "zk", "next", "poly"]

thresholds = {'tps': [1.01, 5, 10, 29.9],
              'withdrawal_time': [60, 10, 1, 0.1],
              'secure_transaction': [60, 12, 5, 1],
              "fee": [0.01, 0.09, 0.5, 2],
              'reputation': [2, 3, 4, 5]}


f_df = read_metrics(static_path, dynamic_path, l2_names)

print("\nRemember the units of the metrics:\n"
          "TPS: transactions per second\n"
          "withdrawl_time: how many minutes does it take to get funds from L2 to L1\n"
          "secure_transaction: How many minutes does it take to savely assume a transaction is part of the Blockchain\n"
          "transaction_fee: How much Dollar costs a transaction\n"
          "reputation: Set by author, whole numbers between 1 and 5")
f_df, old_conditions = filter_dataframes(f_df)

weights = metric_weight(f_df)

comp_df = comparable_metrics(f_df, thresholds)

metrics = list(thresholds.keys())
score = score_calculation(comp_df, metrics, weights)

x = decision(score, f_df, weights,metrics)


watcher(old_conditions, weights)


print("#")