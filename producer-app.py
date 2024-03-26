import os
from confluent_kafka import Producer

producer_conf = {
    "bootstrap.servers":"localhost:9092"
}
producer = Producer(producer_conf)

producer.produce('HelloWorld', key='1', value='Unique message from key 1')
producer.poll(1)


# kafka-topics --bootstrap-server broker:29092 --create --topic HelloWorld 
# --if-not-exists --replication-factor 1 --partition 1
