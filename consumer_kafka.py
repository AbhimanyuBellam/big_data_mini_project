from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

import pandas

consumer = KafkaConsumer(
    'test',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))


client = MongoClient('localhost:27017')
collection = client.numtest2

count=0


for message in consumer:
    count=count +1
    if ( count==999):
        break
    # print (count)
    message = message.value
    #print (message)

    collection.table1.insert(message)
    print('{} added to {}'.format(message, collection))


