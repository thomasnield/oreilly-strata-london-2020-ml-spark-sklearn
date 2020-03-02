import pandas as pd

# TODO: Cover skew in slides
# Skew is a measure of how asymmetrical the data is
# A skew of 0.0 indicates no skew and resembles a perfect bell curve
# Positive and negative numbers indicate a skew to the right or left respectively
dataset = pd.read_csv('../data/employee_retention_analysis.csv', delimiter=",")

skew = dataset.skew()

print(skew)