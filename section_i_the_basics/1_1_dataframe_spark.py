from pyspark.sql import SparkSession

# Creates or retrieves existing Spark session
# and runs it locally with four cores

spark = SparkSession.builder \
    .master("local[4]") \
    .appName("My Spark Model") \
    .getOrCreate() # Creates a new or existing Spark instance

# Find the sum of each number between 0 through 4999
# and returns it as a DataFrame with a single value
df = spark.read.csv("C:\git\oreilly-strata-london-2020-ml-spark-sklearn\data\wildlife-strikes.csv")

print(df.collect())