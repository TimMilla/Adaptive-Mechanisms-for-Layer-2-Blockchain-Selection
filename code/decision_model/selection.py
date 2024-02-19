import pandas as pd

def selecter(df):
    """
    Select the row with the highest score and flag value of 1.
    If the highest score has a flag value of 0, select the next highest score with a flag value of 1,
    and so on until no such entry is left.

    Parameters:
        df (DataFrame): The DataFrame containing the data.

    Returns:
        int: The value from the 'layer_2' column of the selected row.
    """
    # Filter rows where flag is 1
    df = df[df['flag'] == 1]

    # Sort DataFrame by score column in descending order
    df = df.sort_values(by='score', ascending=False)

    # Iterate through rows
    for _, row in df.iterrows():
        if row['flag'] == 1:
            return row['layer_2']

    return None  # Return None if no suitable entry is found