import pandas as pd
from matplotlib import pyplot

# We want to plot a histogram of every variable just to see how the values distribute
# Ideally we want normal distributions but this is not going to happen as often as we'd like
# We can use them anyway to see if there are outliers or other strange occurrences

dataset = pd.read_csv('../data/employee_retention_analysis.csv', delimiter=",")

dataset.hist()
pyplot.show()