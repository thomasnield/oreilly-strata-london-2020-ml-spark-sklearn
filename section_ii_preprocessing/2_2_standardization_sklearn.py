import pandas as pd
from sklearn.preprocessing import StandardScaler

'''
Another transformation that can be done is standaridization, which fits each 
input column to a standard normal distribution and makes each value expressed
in terms of standard norml deviations. This only works if the data is actually 
normally distributed. 

Note this does not make sense to use for binary (1,0) variables. 
'''
df = pd.read_csv('../data/diabetes.csv', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# Rescale all the input variables to be between 0 and 1
scaler = StandardScaler().fit(X)
rescaled_X = scaler.fit_transform(X)

print(rescaled_X)