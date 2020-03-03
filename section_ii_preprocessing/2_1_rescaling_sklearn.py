import pandas as pd
from sklearn.preprocessing import MinMaxScaler

'''
In ML, it is often necessary to not just turn all values into numbers (e.g. turn text into numerical categories)
but also make these numbers fall into the same number range (commonly between 0.0 and 1.0). 
This is helpful for optimization-based machine learning algorithms we will learn about later. 
'''
df = pd.read_csv('../data/employee_retention_analysis.csv', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, 5th column)
Y = df.values[:, 4]

# Rescale all the input variables to be between 0 and 1
scaler = MinMaxScaler(feature_range=(0.0, 1.0))
rescaled_X = scaler.fit_transform(X)

print(X)