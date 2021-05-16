from consumer_kafka_abhinav import get_nearest_busses#listen_cont
# from consumer_kafka_abhinav import 
from kafka_listen_abhinav import listen_cont
import time
from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
# from kafka_listen_abhinav import listen_cont
import pandas
nearest_bus = get_nearest_busses(25,[30,30])
print(nearest_bus)
print("hello")
bus_no = nearest_bus

