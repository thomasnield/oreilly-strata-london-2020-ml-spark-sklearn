"""

# TODO: Create slides, sources for inspiration:
# https://www.youtube.com/watch?v=FgakZw6K1QQ
# https://learning.oreilly.com/library/view/hands-on-machine-learning/9781492032632/ch08.html
# https://machinelearningmastery.com/calculate-principal-component-analysis-scratch-python/
"""

import pandas as pd
from sklearn.decomposition import PCA

df = pd.read_csv('../data/diabetes.csv', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)
Y = df.values[:, -1]

# feature extraction
pca = PCA(n_components=3)
fit = pca.fit(X)

# summarize components
print("Explained Variance: %s" % fit.explained_variance_ratio_)

print(fit.components_)