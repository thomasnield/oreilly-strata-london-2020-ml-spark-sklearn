import pandas as pd

# TODO: Cover Pearson Correlation on Slides, and other correlation topcs in general
# Set every variable against every other variable to see its correlation
# A correlation of 1.0 indicates a perfect positive correlation
# A correlation of -1.0 indicates a perfect negative correlation

dataset = pd.read_csv('../data/employee_retention_analysis.csv', delimiter=",")

correlations = dataset.corr(method='pearson')

print(correlations)