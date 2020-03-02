from pyspark.sql import SparkSession

# Creates or retrieves existing Spark session
# and runs it locally with four cores

spark = SparkSession.builder \
    .master("local[4]") \
    .appName("My Spark Model") \
    .getOrCreate() # Creates a new or existing Spark instance

# Find the sum of each number between 0 through 4999
# and returns it as a DataFrame with a single value
my_sum = spark.range(1, 5000).where("id > 500").selectExpr("sum(id) as my_sum").collect()

print(my_sum)