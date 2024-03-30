import os
import time
import random
from confluent_kafka import Producer

# Kafka producer configuration
producer_conf = {
    "bootstrap.servers": "localhost:9092"
}
producer = Producer(producer_conf)

# Callback function to receive notification of delivery success or failure
def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))

# Function to generate a random message with a message counter
def generate_message(message_counter):
    msg = {
        'MessageNumber': message_counter,  # Include message counter in the message
        'Type': 'key {}'.format(random.randint(1, 10)),
        'Log': '{},{}{}'.format(random.randint(0, 90), random.randint(0, 59), random.choice(['N', 'S'])),
        'Lat': '{},{}{}'.format(random.randint(0, 180), random.randint(0, 59), random.choice(['E', 'W']))
    }
    return msg

# Continuously produce messages
message_counter = 0  # Initialize message counter
while True:
    message_counter += 1  # Increment message counter for each message
    msg = generate_message(message_counter)  # Generate a new random message with the current message counter
    producer.produce(topic='Delivery', key=msg['Type'], value=str(msg), callback=acked)  # Produce the message
    producer.poll(0)  # Poll to handle message delivery asynchronously
    time.sleep(1)  # Sleep for 1 second before producing the next message
