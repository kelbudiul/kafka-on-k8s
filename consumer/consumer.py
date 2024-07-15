from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType

# Define the schema of your Kafka messages
schema = StructType([
    StructField("name", StringType(), True),
    StructField("email", StringType(), True),
    StructField("date", StringType(), True)
])

# Create a Spark session
spark = SparkSession.builder \
    .appName("KafkaConsumer") \
    .getOrCreate()

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "my-kafka-cluster-kafka-bootstrap.kafka:9092") \
    .option("subscribe", "mytopic") \
    .load()

# Parse the value from Kafka
parsed_df = df.select(from_json(col("value").cast("string"), schema).alias("parsed_value"))

# Select the fields you want
output_df = parsed_df.select("parsed_value.*")

# Write the output
query = output_df \
    .writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()