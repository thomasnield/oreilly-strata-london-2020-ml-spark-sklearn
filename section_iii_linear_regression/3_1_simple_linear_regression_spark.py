
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local") \
    .appName("My Spark Model") \
    .getOrCreate()

print(spark.range(5000).where("id > 500").selectExpr("sum(id) as my_sum").collect())