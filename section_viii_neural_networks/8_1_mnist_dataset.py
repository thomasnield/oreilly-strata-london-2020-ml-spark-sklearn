import pandas as pd
from sklearn.ensemble import ExtraTreesClassifier

# load data
df = pd.read_csv('../data/mnist_784.csv', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# Use ExtraTreesClassifier which uses a random forest
# to score importance of each feature
model = ExtraTreesClassifier(n_estimators=100)
model.fit(X, Y)

# Display results
print(pd.DataFrame({'FEATURE': df.columns[0:-1], 'IMPORTANCE': model.feature_importances_}))