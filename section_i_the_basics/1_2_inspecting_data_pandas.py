# Load CSV using Pandas
import pandas as pd

dataset = pd.read_csv('../data/employee_retention_analysis.csv', delimiter=",")

print("First 5 rows:")
print(dataset.head(5))

print("\nDimensions (rows,cols)")
print(dataset.shape)

print("\nData Types:")
print(dataset.dtypes)

print("\nDescription:")
print(dataset.describe())

print("\nClassification Imbalance:")
print(dataset.groupby('DID_QUIT').size())