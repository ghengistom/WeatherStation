import datetime
import hashlib
import sqlite3
import time
import random
from w1thermsensor import W1ThermSensor
from time import gmtime, strftime
import json


#create 64bit hash for pi id
# hash = hashlib.sha1("my message".encode("UTF-8")).hexdigest()
# print(hash)
# print(len(hash))


def gettemp_():
    for sensor in W1ThermSensor.get_available_sensors():
        while True:
            conn = sqlite3.connect('weatherdatabase.db')
            c = conn.cursor()

            unix = int(time.time())
            date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

        #commit and close connection for local db

            sensor = W1ThermSensor()
            temperature_in_celsius = sensor.get_temperature()
            jsonTest = json.loads(str(temperature_in_celsius))
            temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)
      

        #insert a row of data into local db
            c.execute('''INSERT INTO timetemp( time, temp )
                   VALUES(?,?)''', (date, temperature_in_fahrenheit))
       
        #print('Print jsonTest '  + str(jsonTest))
            print('The temperature from new API is '+ str(temperature_in_fahrenheit))
        #print('This is the temp is all units' + str(temperature_in_all_units))

            tojson = json.dumps(temperature_in_fahrenheit)
            #jsonloads = json.loads(str(temperature_in_fahrenheit))
            #print('json.loads format : ' + str(jsonloads))
            conn.commit()
            conn.close()
            return tojson + "  " + date
            
#gettemp_()             #for debugging
            
            
