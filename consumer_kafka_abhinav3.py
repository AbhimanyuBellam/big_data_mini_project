from kafka_listen_abhinav import listen_cont
bus_no = 71
lat,lon,time = listen_cont(bus_no)
print("working")
print(lat,lon,time)
