from flask import Flask
from flask_restful import Api, Resource, reqparse

from consumer_kafka_abhinav import get_nearest_busses#listen_cont
# from consumer_kafka_abhinav import 
# from kafka_listen_abhinav import listen_cont
import time
from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads
import json
# from kafka_listen_abhinav import listen_cont
import pandas

app = Flask(__name__)
api = Api(app)

users = [
    {
        "name": "Jass",
        "age": 22,
        "occupation": "Web Developer"
    }
]

from flask import jsonify

class Search_bus(Resource):
    def get(self, route,lat,lon):
                bus_no  = get_nearest_busses(route,[lat,lon])
                a = {"bus_no":str(bus_no)}
                aj = json.dumps(a)
                return aj,200
        

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200

from kafka_listen_abhinav import listen_cont

class Listen_bus(Resource):
    def get(self,bus_no):
                lat,lon ,time = listen_cont(bus_no)
                a = {"bus_no":str(bus_no),"lat":str(lat),"lon":str(lon),"time":str(time)}
                aj = json.dumps(a)
                return aj, 200
        

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists".format(name), 400

        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
        
        user = {
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }
        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200


# api.add_resource(User, "/user/<string:name>")
api.add_resource(Search_bus,"/search/<int:route>/<int:lat>/<int:lon>")
api.add_resource(Listen_bus,"/listen/<int:bus_no>")
# api.add_resource(User,"/search_bus/<string:route_no>")
# api.add_resource(User,"/listen_bus/<string:bus_no>")
app.run("10.59.98.242")