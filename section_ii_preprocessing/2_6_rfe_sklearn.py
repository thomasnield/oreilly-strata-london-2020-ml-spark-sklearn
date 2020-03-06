"""
We can select features a bit more aggressively based on a specific machine learning model
and how well each given feature contributes to that model accuracy.

Using recursive feature elimination (RFE), we can select the top K variables based on a specific machine
learning model (e.g. logistic regression) and recursively eliminate less impactful variables.

https://scikit-learn.org/stable/modules/feature_selection.html#rfe
"""

import pandas as pd
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
df = pd.read_csv('../data/employee_retention_analysis.csv', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# Extract the top 2 features that impact the outcome the most
model = LogisticRegression(solver='liblinear')
rfe = RFE(model, 2)
fit = rfe.fit(X, Y)

print("Selected Features: %s" % fit.support_)
print("Feature Ranking: %s" % fit.ranking_)

