import pymongo
import argparse

#ap
ap = argparse.ArgumentParser()
ap.add_argument("-r", "--route", required=True,
	help="route of the bus")

ap.add_argument("-w", "--time", required=True,
	help="Time (24-hour-time-format)")

args = vars(ap.parse_args())

#mogo querey
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["numtest2"]
mycol = mydb["table1"]

myquery = { 'route_no': int(args["route"]),
            'timestamp': int(args["time"])}
print(myquery)
mydoc = mycol.find(myquery)


#append requested rows in an array
requested_list = []
for x in mydoc:
    requested_list.append(x)
    
#cal speed - input params - lat long
def cal_speed(long_list , lat_list):
    pass