import pandas as pd
import os

def read_metrics(static_path, dynamic_path, l2_solutions, l2_name="layer_2", watcher=0):
    """

    :param static_path:
    :param dynamic_path:
    :param l2_solutions:
    :param l2_name:
    :param watcher:
    :return:
    """

    ## READ DATA ##
    # READ more data if new metrics are included

    # first read static data
    os.chdir(static_path)
    static_data = pd.read_excel("static_data.xlsx")

    # secondly read dynamic data
    os.chdir(dynamic_path)
    dynamic_data_tps = pd.read_excel("tps.xlsx")
    dynamic_data_fee =pd.read_excel("transaction_fee.xlsx")

    # return to original path
    #os.chdir(os.path.dirname(os.path.realpath(__file__)))
    os.chdir(os.path.dirname(static_path))

    ## COMBINE static and dynamic data ##

    # save static metrics in final dataframe
    final_df = static_data.copy()

    # create temporal dictionary for every dynamic metric
    # ADD more dictionaries if more dynamic data is included
    tmp_dic_fee = {}
    tmp_dic_tps = {}

    # calculate dynamic data
    for col in l2_solutions:
        # save temporal value
        # fee
        tmp_fee = dynamic_data_fee[col].mean()
        # tps
        # take mean
        tmp_mean_tps = dynamic_data_tps[col].mean()
        # number of entries -> number of data points
        num_entries = len(dynamic_data_tps)
        # current data is tps per day -> seconds per day
        # CHANGE if underlying data is different!
        #calculate tps
        tmp_tps = tmp_mean_tps / (num_entries*24*60*60)


        # add it to temporal dictionaries
        tmp_dic_fee[col] = tmp_fee
        tmp_dic_tps[col] = tmp_tps

    # save calculated dynamic data in final dataframe
    final_df["tps"] = final_df["layer_2"].map(tmp_dic_tps)
    final_df["fee"] = final_df["layer_2"].map(tmp_dic_fee)

    #EXPORT

    return final_df


