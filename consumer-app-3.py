#This is another consumer, in a different consumer group

from confluent_kafka import Consumer

conf = {"bootstrap.servers":"localhost:9092",
        'group.id': '2',
        'auto.offset.reset': 'earliest'}

consumer = Consumer(conf)
consumer.subscribe(['Delivery'])

running = True

while running:
    msg = consumer.poll(1)
    if msg is None: continue
    else:
        print(msg.value())