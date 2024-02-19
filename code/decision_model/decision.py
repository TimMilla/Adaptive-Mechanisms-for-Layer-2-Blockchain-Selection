import pandas as pd
import os
from datetime import datetime
from .selection import selecter




# main function

def decision(score_df, value_df, weights,metric_names):

    # decision
    solution = selecter(score_df)

    # export .xlsx file
    # Get the current working directory
    current_dir = os.getcwd()
    # Define the path to the "results" subfolder
    results_dir = os.path.join(current_dir, 'results')

    # Create the "results" subfolder if it doesn't exist
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)


    # Get current date and time
    now = datetime.now()
    # Format the filename
    filename = f"sm_{now.strftime('%d_%m_%y_%H_%M_%S')}.xlsx"
    output_file_path = os.path.join(results_dir, filename)

    # Create a Pandas Excel writer using XlsxWriter as the engine
    writer = pd.ExcelWriter(output_file_path, engine='xlsxwriter')

    # Write each DataFrame to a separate worksheet
    value_df.to_excel(writer, sheet_name='Value', index=False)
    score_df.to_excel(writer, sheet_name='Score', index=False)
    pd.DataFrame({'Weights': weights}).to_excel(writer, sheet_name='Weights', index=False)

    # Calculate row index where each DataFrame ends
    value_df_end = len(value_df) + 1  # Add 1 to account for header row
    score_df_end = value_df_end + len(score_df) + 2  # Add 2 for the 2-line gap
    weights_df_end = score_df_end + len(weights) + 2  # Add 2 for the 2-line gap

    # Write the solution variable
    worksheet = writer.sheets['Weights']
    worksheet.write(weights_df_end, 0, f'solution: {solution}')

    # Save the Excel file
    writer.save()


    return solution