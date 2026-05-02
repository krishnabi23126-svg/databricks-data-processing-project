from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("StreamingPipeline").getOrCreate()

# Read streaming data
df = spark.readStream.format("json").load("data/")

# Transform
df_transformed = df.groupBy("product").sum("amount")

# Output
query = df_transformed.writeStream \
    .format("console") \
    .outputMode("complete") \
    .start()

query.awaitTermination()
