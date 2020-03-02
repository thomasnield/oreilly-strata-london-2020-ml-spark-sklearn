# Load CSV using NumPy
from numpy import loadtxt
from urllib.request import urlopen

raw_data = urlopen('../data/employee_retention_analysis.csv')
dataset = loadtxt(raw_data, delimiter=",", skiprows=1)
print(dataset)
