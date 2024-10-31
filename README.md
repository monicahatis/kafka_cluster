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
In a Kafka system, consumers within the same consumer group are assigned to consume messages from different partitions within a topic. Each consumer is responsible for processing messages from one or more partitions independently. If there are more partitions than consumers in a group, each consumer may handle messages from multiple partitions. Conversely, if there are more consumers than partitions, some consumers may remain idle until additional partitions become available. This partition-based assignment ensures efficient parallel processing of messages within a consumer group while maintaining independent consumption across consumers.

#### Consumer 1
Consumes messages from the 'Delivery' topic within consumer group 1.

#### Consumer 2
Consumes messages from the 'Delivery' topic within consumer group 1.

#### Consumer 3
Consumes messages from the 'Delivery' topic within consumer group 2.

## Short Notes on kafka consumer groups and consumers
In Apache Kafka, consumer groups allow multiple consumers to read from the same topic while maintaining a single logical subscription. Here's how Kafka behaves when you have two consumer groups, with one of those groups having several consumers:

### Key Concepts
#### Consumer Group:

A consumer group is a set of consumers that work together to consume messages from one or more Kafka topics.
Each consumer in a group reads from a different partition of the topic, ensuring that each message is processed by only one consumer in that group.

#### Partitions:

Kafka topics are divided into partitions, and messages within each partition are ordered.
A partition can be consumed by only one consumer in a consumer group at a time.

#### Behavior with Two Consumer Groups
##### Scenario:
Consumer Group A: Has several consumers (e.g., Consumer A1, A2, A3).
Consumer Group B: Has one consumer (e.g., Consumer B1).

##### Message Consumption:
###### Independent Consumption:

Both consumer groups operate independently. This means that Consumer Group A and Consumer Group B can consume the same messages from the topic without affecting each other.
If a message is published to a topic, both Consumer Group A and Consumer Group B will receive that message, regardless of how many consumers are in each group.

###### Load Balancing Within a Consumer Group:

Within Consumer Group A, the consumers (A1, A2, A3) will divide the partitions among themselves. For example:
If the topic has 6 partitions, the consumers will consume messages from their assigned partitions.
If Consumer A1 is assigned partitions 0 and 1, A2 is assigned partitions 2 and 3, and A3 is assigned partitions 4 and 5, each consumer will read messages only from its assigned partitions.

#### Offset Management:

Each consumer group maintains its own offsets. This means that Consumer Group A and Consumer Group B can have different read positions in the topic.
When a consumer in a group reads a message, it commits the offset, allowing it to remember where it left off for the next read. This offset is unique to each consumer group.

#### Scaling:

If you add more consumers to Consumer Group A, Kafka will reassign the partitions among the consumers in that group. If the number of consumers exceeds the number of partitions, some consumers will remain idle.
Consumer Group B remains unaffected by changes in Consumer Group A.

### Summary
In summary, when you have two consumer groups in Kafka, each group consumes messages independently from the same topic, allowing for parallel processing. Consumers within a group share the load by distributing partitions among themselves, while offsets are managed separately for each group. This architecture allows Kafka to provide both high throughput and scalability for message processing.


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

#### Troubleshooting
Here are some errors I had encountered and how to solve them
$${\color{red}Welcome \space \color{lightblue}To \space \color{orange}Stackoverflow}$$

$${\color{red}Cannot\space \ connect\space \ to\space \ the \space \ Docker \space \ daemon \space \ at \space \ unix:///home/.docker/desktop/docker.sock. Is\space \ the \space \ docker \space \ daemon \space \ running?}$$

How to start docker
If you're on a Linux-based system, you can start the Docker daemon by running:
```
sudo systemctl start docker
```
On Windows or macOS, open the Docker Desktop application, as it should automatically start the daemon.

Check the Docker Daemon Status: To verify if Docker is running (on Linux):

```
sudo systemctl status docker
```

If it’s not running, you can enable it to start on boot:

```
sudo systemctl enable docker
```

For my commands I was using 'sudo' due to permission issues.
You can add your user to the docker group to allow Docker commands without sudo:

```
sudo usermod -aG docker $USER
```
Then, log out and log back in to apply the group changes.

Restart Docker Desktop (for macOS/Windows): If you're using Docker Desktop, a simple restart of the application often resolves connectivity issues.


Another error I faced:

$${\color{red}Creating \space \ network \space \ "kafka-cluster_default" \space \ with \space \ the \space \ default \space \ driver \space \
Creating \space \ zookeeper ... error \space \

ERROR: \space \ for \space \ zookeeper \space \ Cannot \space \ create \space \ container \space \ for \space \ service \space \ zookeeper: \space \ Conflict. \space \ The \space \ container \space \ name \space \ "/zookeeper" \space \ is \space \ already \space \ in \space \ use \space \ by \space \ container \space \ "bf3865684ac0779c2db17d28b6a3f6d764462e6080ade7e27f91da438b493cd3". \space \ You \space \ have \space \ to \space \ remove \space \ (or \space \ rename) \space \ that \space \ container \space \ to \space \ be \space \ able \space \ to \space \ reuse \space \ that \space \ name.

ERROR: \space \ for \space \ zookeeper \space \ Cannot \space \ create \space \ container \space \ for \space \ service \space \ zookeeper: \space \ Conflict. \space \ The \space \ container \space \ name \space \ "/zookeeper" \space \ is \space \ already \space \ in \space \ use \space \ by \space \ container \space \ "bf3865684ac0779c2db17d28b6a3f6d764462e6080ade7e27f91da438b493cd3". You \space \ have \space \ to \space \ remove \space \ (or \space \ rename) \space \ that \space \ container \space \ to \space \ be \space \ able \space \ to \space \ reuse \space \ that \space \ name.}$$

This error occurs because there’s already a running (or previously created) container named "zookeeper," which conflicts with your current attempt to create or start a new one. Here’s how you can resolve it:

Identify Running Containers:

```
docker ps -a
```
This command lists all containers, including stopped ones, and will allow you to see the conflicting container ID and its status.

Remove the Conflicting Container: You can remove the conflicting container by using its ID (in this case, bf3865684ac0779c2db17d28b6a3f6d764462e6080ade7e27f91da438b493cd3):

```
docker rm bf3865684ac0779c2db17d28b6a3f6d764462e6080ade7e27f91da438b493cd3
```
(Alternative) Stop and Remove All Containers: If there are multiple containers, or if you’re not sure which is causing issues, you can stop and remove all containers:

```
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)

```
Start Docker Compose Again: After clearing up the conflicting containers, you can restart your project:

```
docker-compose up
```
These steps should help resolve the conflict and get your containers running.
