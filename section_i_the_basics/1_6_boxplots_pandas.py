import pandas as pd
from matplotlib import pyplot
from pandas.plotting import scatter_matrix

'''
Scatter matrices are one of the most helpful tools for doing machine learning analysis.
They plot a scatterplot between each pair of variables and it's easy to see eyeball patterns and correlations.
Note that variables intersecting themselves will just show a histogram.
'''

dataset = pd.read_csv('../data/employee_retention_analysis.csv', delimiter=",")
scatter_matrix(dataset)
pyplot.show()