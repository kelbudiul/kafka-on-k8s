# Kafka-Spark Streaming Project

## Overview
This project implements a data streaming pipeline using Apache Kafka and Apache Spark. It generates fake user data, streams it through Kafka, processes it with Spark, and stores it in a PostgreSQL database.

## Components
- **Kafka Producer**: Generates fake user data and sends it to a Kafka topic.
- **Kafka Consumer**: Uses Spark Structured Streaming to consume data from Kafka and process it.
- **PostgreSQL**: Stores the processed data.
- **Monitoring**: Uses Prometheus and Grafana for metrics and visualization.

## Prerequisites
- Docker and Docker Compose
- Kubernetes cluster
- Helm 3

## Project Structure
```
.
├── producer/
│   ├── producer.py
│   └── Dockerfile
├── consumer/
│   ├── consumer.py
│   └── Dockerfile
├── helm/
│   └── kafka-spark-streaming/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           ├── service.yaml
│           └── configmap.yaml
├── README.md
└── docker-compose.yml
```

## Setup and Installation

### Local Development
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Start the local environment: `docker-compose up -d`
4. Run the producer: `python producer/producer.py`
5. Run the consumer: `python consumer/consumer.py`

### Kubernetes Deployment
1. Ensure your Kubernetes cluster is running and `kubectl` is configured
2. Install the Helm chart:
   ```
   helm install my-kafka-spark-app helm/kafka-spark-streaming
   ```

## Configuration
- Kafka configuration can be modified in `helm/kafka-spark-streaming/values.yaml`
- Database connection details should be set as environment variables or Kubernetes secrets

## Monitoring
Access Grafana at `http://<your-grafana-url>` to view dashboards for Kafka and Spark metrics.

## Troubleshooting
- Check Kafka logs: `kubectl logs -f <kafka-pod-name>`
- Check Spark logs: `kubectl logs -f <spark-pod-name>`
- Ensure all services are running: `kubectl get pods`
