import os
import pandas as pd

# helper function
def bucket_value(value, threshold_list):
    """

    :param value:
    :param threshold_list:
    :return:
    """
    if value <= threshold_list[0]:
        return 1
    elif value > threshold_list[-1]:
        return 5
    else:
        for i in range(1, len(threshold_list)):
            if threshold_list[i-1] < value <= threshold_list[i]:
                return i + 1

# main function
def comparable_metrics(df, thresholds):
    """

    :param df:
    :param thresholds:
    :return:
    """
    final_df = df.copy()
    for col in df.columns:
        # skip variables that are not metrics
        if col in ["layer_2", "flag"]:
            continue
        #
        final_df[col] = df[col].apply(lambda x: bucket_value(x, thresholds[col]))

    return final_df