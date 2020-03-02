import pandas as pd
from matplotlib import pyplot

# To smooth out our histograms and see our data in a probability distribution
# We can use density plots, which will be much cleaner to see than the histograms

dataset = pd.read_csv('../data/employee_retention_analysis.csv', delimiter=",")

dataset.plot(kind='density', subplots=True, layout=(2,3), sharex=False)
pyplot.show()