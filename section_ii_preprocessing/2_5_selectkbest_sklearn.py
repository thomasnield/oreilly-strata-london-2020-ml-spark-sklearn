"""
We need to choose which features (input variables) we want to use
for our machine learning prediction. If we want to do this automatically, we can
use SelectKBest (choose best K number of features) or SelectPercentile (choose highest scoring features within percentile).

Within those functions, we can choose the implementation:
For regression: f_regression, mutual_info_regression
For classification: chi2, f_classif, mutual_info_classif

https://scikit-learn.org/stable/modules/feature_selection.html#univariate-feature-selection
https://blog.minitab.com/blog/adventures-in-statistics-2/understanding-analysis-of-variance-anova-and-the-f-test

Explanation of Chi-Square: https://www.youtube.com/watch?v=VskmMgXmkMQ
"""

import pandas as pd
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('../data/iris.csv', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# Extract the top 2 features that impact the outcome the most
fit = SelectKBest(score_func=chi2, k=2).fit(X,Y)

print(fit.scores_)
features = fit.transform(X)

print(features)
