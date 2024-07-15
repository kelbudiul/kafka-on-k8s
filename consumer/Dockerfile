FROM apache/spark-py:v3.3.2

USER root

# Install necessary Python packages
RUN pip install kafka-python

# Copy the PySpark script
COPY . /app/

# Set the working directory
WORKDIR /app

# Run the PySpark script
CMD ["spark-submit", "--packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.2", "pyspark_consumer.py"]
