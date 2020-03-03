# Load CSV using Pandas and SQL
import pandas as pd
import sqlite3

# We are using the built-in Python SQLite driver to connect to a SQLite database file
# Python should have a standardized DBI interface for whatever SQL platform you use

conn = sqlite3.connect('../data/flight_delays.db')

dataset = pd.read_sql("SELECT * FROM airport", conn)

print(dataset)
