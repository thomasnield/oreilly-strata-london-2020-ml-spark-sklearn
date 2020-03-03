import pandas as pd
from sklearn.preprocessing import Normalizer

'''
We can also use normalization which is slightly more complicated. 
This rescales the input variables so the resulting vector has a length of 1. 
For example, for a point (x1,x2) has a given value (2,2), 
this would be transformed to (.70710678, .70710678) 
because the hypotenuse from the origin will be 1.0. 

This works best for sparse datasets with attributes of many scales, 
for neural networks, k-nearest neighbors, and other ML algorithms. 
'''
df = pd.read_csv('../data/diabetes.csv', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# Rescale all the input variables to be normalized
# This
scaler = Normalizer().fit(X)
rescaled_X = scaler.fit_transform(X)

print(rescaled_X)
