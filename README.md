# Simple Kafka cluster

Author : Monicah Omondi

## Description

This project provides a Dockerized environment for running Apache Kafka using Docker Compose. It includes configurations for Kafka broker, Zookeeper, a producer script, and multiple consumer scripts. Confluent Kafka is utilized in this project 


## Services

### Zookeeper
Zookeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. It is required for Kafka to function properly.

Image: confluentinc/cp-zookeeper:7.3.0

Hostname: zookeeper

Port: 2181

### Broker
The Kafka broker is responsible for receiving and storing messages from producers, as well as serving them to consumers.

Image: confluentinc/cp-server:7.3.0

Hostname: broker

Ports:

9092: Kafka broker listener port

9101: Kafka broker REST port

29092: Kafka inter-broker communication port

### Producer Script
The producer script (producer.py) generates random messages and publishes them to a Kafka topic named 'Delivery'.

### Consumer Scripts

#### Consumer 1
Consumes messages from the 'Delivery' topic within consumer group 1.

#### Consumer 2
Consumes messages from the 'Delivery' topic within consumer group 1.

#### Consumer 3
Consumes messages from the 'Delivery' topic within consumer group 2.



## Running the project locally

### Prerequisites
Before running the Kafka Docker containers, ensure you have Docker and Docker Compose installed on your system.

#### Commands
Clone this repository to your local machine:
```
git clone <repository_url>
```

Run Docker Compose to start the Kafka services:
```
docker-compose up 
```
Verify that the Docker containers are running:
```
docker ps
```
Navigate to the kafka container
```
docker exec -it <container id> bash
```
In this project we are creating a topic manually. This is not good practice but just for learning purpose.

While still in the kafka container, run this command
```
kafka-topics --bootstrap-server broker:29092 --create --topic Delivery --if-not-exists --replication-factor 1 --partitions 2
```
Run the producer script
```
python3 producer.py
```
Run the different consumer scripts
```
python3 <script name>
```
