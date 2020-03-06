"""
Since machine learning expects all variables to be converted into numbers,
we sometimes have to find ways to turn non-numeric data (e.g. strings) into numbers.
For example, the iris data set has a 'species' column which is text.

Since the species column is categorical, we can assign an integer for each category
and transform accordingly (e.g. setosa = 0, versicolor = 1, virginica = 2).

Note that scikit-learn will do this automatically for us in many parts of its API.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('../data/iris.csv', delimiter=",")

# LabelEncoder will turn categorical labels into integers
LE = LabelEncoder()
df['species'] = LE.fit_transform(df['species'])

print(df)