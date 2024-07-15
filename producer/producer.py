from kafka import KafkaProducer
from faker import Faker
import json
import time

# Create a Faker instance
fake = Faker()

# Create a Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['my-kafka-cluster-kafka-bootstrap.kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Generate and send fake data
while True:
    data = {
        "name": fake.name(),
        "email": fake.email(),
        "date": fake.date_time_this_year().isoformat()
    }
    producer.send('mytopic', data)
    print(f"Sent: {data}")
    time.sleep(1)  # Wait for 1 second before sending the next message
