import pymongo
import argparse

#ap
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--route", required=True,
	help="route of the bus")
ap.add_argument("-time", "--time", required=True,
	help="Time (24-hour-time-format)")
args = vars(ap.parse_args())

#modify
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

#query from user
myquery = { "Route Number": args["route"],
            "Time": args["time"]}


mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)

 
