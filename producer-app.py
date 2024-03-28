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

    'Type': 'Truck 1',
    'Log': '67,8N',
    'Lat': '56.7s'
}

producer.produce(topic='Delivery', partition=0, value= str(msg), callback=acked)
producer.poll(1)
#Message cant be sent twice in the scenario it was sent the first time and didnt go(connection not established) but remained in queue. When the producer produces again the messages end up being two
#producer.flush()


#in a real world we dont do this manually, creating a kafka topic:   kafka-topics --bootstrap-server broker:29092 --create --topic HelloWorld 
# --if-not-exists --replication-factor 1 --partition 1


##This file is not within the docker env
#the producer will connect with the advertised listener