import os
import pandas as pd

def metric_weight(dataframe):
    weights = []

    # get metric names
    exclude_names = ['flag', 'layer_2']
    # Get all column names and filter out the excluded names
    metrics = [col for col in dataframe.columns if col not in exclude_names]

    # Standard weight
    for _ in range(len(metrics)):
        weights.append(1)

    print("In the following you are able to determine weights for the automatically selection of \n"
          "layer-2 solutions. Give a metric a higher weight if this metric is more important. If a metric\n"
          "is unimportant give it a lower number.")
    confirmation = input("Do you want to enter weights for metrics? (yes/no): ")
    if confirmation.lower() != "yes":
        print("Exiting the program.")
    else:
        # Loop through metrics
        for count, i in enumerate(metrics):
            while True:
                try:
                    # User input for weight
                    weight = float(
                        input("Give a weight for the metric '{}': Enter a number between 0 and 5: ".format(i)))
                    if 0 <= weight <= 5:
                        # If number is valid, append to weights and exit the loop
                        weights[count] = weight
                        break
                    else:
                        print("The input number has to be in the range of 0 to 5.")
                except ValueError:
                    print("Invalid input. Only enter a number between 0 and 5.")
    return weights