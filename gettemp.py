import datetime
import hashlib
import sqlite3
import time
import random
from w1thermsensor import W1ThermSensor
from time import gmtime, strftime
import json


#create 64bit hash for pi id
hash = hashlib.sha1("my message".encode("UTF-8")).hexdigest()
print(hash)
print(len(hash))


for sensor in W1ThermSensor.get_available_sensors():
    while True:
        print('in while loop')
        conn = sqlite3.connect('weatherdatabase.db')
        c = conn.cursor()
        far = sensor.get_temperature()*9/5 + 32 
        print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))
        print(far)

        #insert a row of data into local db
        unix = int(time.time())
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
#        keyword = 'Python'
#        value = random.randrage(0,10)

        c.execute('''INSERT INTO timetemp( time, temp )
                   VALUES(?,?)''', (date, far))

        #commit and close connection for local db
        from w1thermsensor import W1ThermSensor

        sensor = W1ThermSensor()
        temperature_in_celsius = sensor.get_temperature()
        temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
        temperature_in_all_units = sensor.get_temperatures([
            W1ThermSensor.DEGREES_C,
            W1ThermSensor.DEGREES_F,
            W1ThermSensor.KELVIN])    
       
        print('The temperature from new API is '+ str(temperature_in_fahrenheit))

        conn.commit()
        time.sleep(20)
        conn.close()
        
print("all done")
