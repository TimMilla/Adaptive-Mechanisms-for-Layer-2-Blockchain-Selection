import pandas as pd


def score_calculation(df, columns_to_consider, weights):
    """
    Calculate scores for each row in the DataFrame based on specified columns and multipliers.

    Parameters:
        df (DataFrame): The DataFrame containing the data.
        columns_to_consider (list): List of column names to consider for score calculation.
        weights (list): List of multipliers corresponding to the columns to consider.

    Returns:
        DataFrame: A new DataFrame with an additional 'Score' column containing the calculated scores.
    """

    # Helper-Function to calculate score for each row
    def calculate_score(row):
        score = 0
        for col, value in row.items():
            if col in columns_to_consider:
                index = columns_to_consider.index(col)
                score += value * weights[index]
        return score

    # Create new column with calculated scores
    df['score'] = df.apply(calculate_score, axis=1)

    return df