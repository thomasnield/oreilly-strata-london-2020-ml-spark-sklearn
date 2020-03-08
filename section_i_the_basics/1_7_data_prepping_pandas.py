import sqlite3

import pandas as pd

df = pd.read_csv('../data/wildlife-strikes.csv')

# Don't limit display of rows or columns
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

# Get rid of records where year is greater than or equal to 2010
df = df[df["Incident Year"] >= 2010]

# Merge Incident Year, Incident Month, Incident Day columns into "incident_date" column
df["incident_date"] = pd.to_datetime(df[["Incident Year", "Incident Month", "Incident Day"]].astype(str).agg('-'.join, axis=1))
df = df.drop(columns= ["Incident Year", "Incident Month", "Incident Day"], axis=1)

# Rename all column names lower case and with underscores _ instead of spaces
renames = { str(c) : str(c).lower().replace(" ", "_") for c in df.columns}
df.rename(renames, axis=1, inplace=True)

print(df.transpose())

# Write to SQLite database
# conn = sqlite3.connect('../data/data_prep.db')
# df.to_sql("wildlife_strikes", conn)