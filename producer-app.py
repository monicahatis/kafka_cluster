import os
from confluent_kafka import Producer

producer_conf = {
    "bootstrap.servers":"localhost:9092"
}
producer = Producer(producer_conf)

#Callback function to receive notification of delivery success or failure
def acked(err, msg):
    if err is not None:
        print("Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("Message produced: %s" % (str(msg)))


msg = {

    'Type': 'key 7',
    'Log': '30,8N',
    'Lat': '27.7s'
}

#producer.produce(topic='Delivery', partition=1, value= str(msg), callback=acked)

#The partition the message goes to isn't defined, There is an algorithm that defines where the message goes to
producer.produce(topic='Delivery', key=msg['Type'], value= str(msg), callback=acked)

producer.poll(1)
#using poll() Message cant be sent twice. When using flash(), in the scenario it was sent the first time and didnt go(connection not established) but remained in queue. When the producer produces again the messages end up being two
#producer.flush()


#in a real world we dont do this manually, creating a kafka topic:   kafka-topics --bootstrap-server broker:29092 --create --topic HelloWorld 
# --if-not-exists --replication-factor 1 --partition 1


##This file is not within the docker env
#the producer will connect with the advertised listener