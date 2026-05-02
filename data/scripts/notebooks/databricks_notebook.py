# Databricks Notebook Simulation

# Load data
df = spark.read.json("/FileStore/data/streaming_data.json")

# Transformation
df.createOrReplaceTempView("sales")

result = spark.sql("""
SELECT product, SUM(amount) as total_sales
FROM sales
GROUP BY product
""")

display(result)
