# Load CSV using Pandas
from urllib.request import urlopen
import pandas as pd

raw_data = urlopen('../data/employee_retention_analysis.csv')
dataset = pd.read_csv(raw_data, delimiter=",")
print(dataset)
