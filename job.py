from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

spark = SparkSession.builder.appName("JenkinsDemo").getOrCreate()

df = spark.read.csv("data.csv", header=True, inferSchema=True)

transformed = (
    df.withColumn("value_plus_one", col("value") + 1)
      .withColumn("source", lit("jenkins_demo"))
      .withColumn("value_plus_two", col("value") + 2)
)

transformed.show()

spark.stop()
