import pandas as pd
import os


def filter_dataframes(dataframes, rerun=0, old_condition=[]):
    filtered_dataframes = []  # List for filtered DataFrames
    extra_variables = []  # List for extra variables

    """"
    ADAPTER:
    Input dataframe has to be changed. This done because of an old implementation of the function.
    """
    df_tmp_12 = dataframes.copy()

    # List for smaller DataFrames
    dataframes = []

    # Split DataFrame into smaller DataFrames
    for index, row in df_tmp_12.iterrows():
        smaller_dataframe = pd.DataFrame([row], columns=df_tmp_12.columns)
        dataframes.append(smaller_dataframe)

    """
    ADAPTER END
    """
    df = dataframes[0]  # can select any df, just need the column names

    for i in range(len(dataframes)):
        extra_variables.append(1)

    if rerun == 0:
        print("Would you like to apply a filter for each column? (yes/no)")
        apply_filter_all_columns = input()
    elif rerun == 1:
        apply_filter_all_columns = 'yes'
    else:
        print("ERROR, variable rerun has to be eiter 0 or 1.")

    if apply_filter_all_columns.lower() == 'yes':
        filtered_df = df.copy()  # Create a copy of the original DataFrame to apply the filters
        extra_variable = 1  # Default value for the extra variable

        for count, column in enumerate(df.columns):
            if column == "layer_2":
                continue
            if rerun == 0:
                apply_filter = input(
                    f"Would you like to apply a filter for the '{column}' column of the DataFrame? (yes/no): ")
            else:
                apply_filter = "no"
            if apply_filter.lower() == 'yes':
                if rerun == 0:
                    condition = input(
                        f"Enter a condition for the '{column}' column of the DataFrame (e.g., '>5', '<10', '3-7'): ")
                    old_condition[count] = condition
                else:
                    condition = old_condition[count]
                if condition:
                    if '-' in condition:
                        low, high = map(int, condition.split('-'))
                        for count, df2 in enumerate(dataframes):
                            filtered_df = df2.copy()
                            filtered_df = filtered_df[(filtered_df[column] >= low) & (filtered_df[column] <= high)]
                            # filter not true, mark layer-2 solutions as false
                            if len(filtered_df) == 0:
                                extra_variables[count] = 0
                    elif '>' in condition:
                        value = int(condition[1:])
                        for count, df24 in enumerate(dataframes):
                            filtered_df = df24.copy()
                            filtered_df = filtered_df[filtered_df[column] > value]
                            # filter not true, mark layer-2 solutions as false
                            if len(filtered_df) == 0:
                                extra_variables[count] = 0
                    elif '<' in condition:
                        value = int(condition[1:])
                        for count, df23 in enumerate(dataframes):
                            filtered_df = df23.copy()
                            filtered_df = filtered_df[filtered_df[column] < value]
                            # filter not true, mark layer-2 solutions as false
                            if len(filtered_df) == 0:
                                extra_variables[count] = 0
                    else:
                        print("\nInvalid condition. Please enter one of the following conditions: '>x', '<x', 'x-y'.")
                        print(f"\n No filter is set for {column}")
                        old_condition[count] = None
                else:
                    print("No filter was used.")
                    old_condition[count] = None
    else:
        print("No filter was used")
        old_condition = [None] * len(df.columns)


    """
    ADAPTER:
    Put dataframe back together
    """
    final_df = pd.concat(dataframes, ignore_index=True)
    final_df["flag"] = extra_variables

    return final_df, old_condition