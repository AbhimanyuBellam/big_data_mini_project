from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
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


def listen_cont(bus_no):
    print("listening")
    count = 0
    timestamp = 0
    for message in consumer:
        print("hello")
        message = message.value
        if message['bus_no'] == bus_no :
            print(message)
            time_new = message['timestamp']
            # print("time new",time_new)
            if time_new > timestamp :
                lat = message['latitude']
                lon = message['longtiude']
                timestamp = time_new
            
        count = count + 1
        if count == 499 :
            break

        
        # print('{} added to {}'.format(message, collection))
    return (lat,lon,timestamp)