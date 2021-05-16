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


def get_nearest_busses(route_no,bus_stop):
 

    count=0

    busses = []
    route_no = route_no
    bus_stop_lat = bus_stop[0]
    bus_stop_long = bus_stop[1]
    flag = 0
    dist = 0
    short_bus = 0
    short_dist = 1000
    for message in consumer:
        count=count +1
        if ( count==500):
            break
        # print (count)
        message = message.value
        # print (message)
        rt = message['route_no']
        # print(type(rt))
        if rt == route_no :
            lat = message['latitude']
            lon = message['longtiude']
            dist = ((bus_stop_lat-lat)**2 +(bus_stop_long-lon)**2)**(1/2)
            if flag == 0 :
                flag = 1
                short_dist = dist
                short_bus = message['bus_no']
            else :
                if dist < short_dist :
                    short_dist = dist
                    short_bus = message['bus_no']
        # print("1")
            

    
    
        # print("short bus : ",short_bus,"dist : ",short_dist)
        # collection.table1.insert(message)

    print("short bus : ",short_bus,"dist : ",short_dist)
    return(short_bus)
    # print('{} added to {}'.format(message, collection))


if __name__ == "__main__" :

    nearest_bus = get_nearest_busses(25,[30,30])
