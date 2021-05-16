from time import sleep
from json import dumps
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],api_version=(2,2,1),
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
data=[]
with open('bus_fake_data.json') as f:
	for line in f:
		data.append( json.loads(line))
	
#print (data)

for e in data:
	print (e)
	producer.send('test', value=e)
	

#kafka-docker_kafka_1_dcbf8a05b8bb



