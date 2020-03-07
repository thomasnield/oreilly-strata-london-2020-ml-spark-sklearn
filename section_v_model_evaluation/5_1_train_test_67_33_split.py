import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the data
df = pd.read_csv('../data/employee_retention_analysis.csv', delimiter=",")

# Extract input variables (all rows, all columns but last column)
X = df.values[:, :-1]

# Extract output column (all rows, last column)\

Y = df.values[:, -1]

# Separate training and testing data to evaluate performance and reduce overfitting
# This leaves a third of the data out for testing
# Set a random seed just to make the randomly selected split consistent
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.33, random_state=10)

model = LogisticRegression(solver='liblinear')
model.fit(X_train, Y_train)
result = model.score(X_test, Y_test)
print("Accuracy Mean: %.3f" % result)
