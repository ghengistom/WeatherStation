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

def double_quote(word):
    return '"%s"' % word


def gettemp_():
    for sensor in W1ThermSensor.get_available_sensors():
        while True:
            
            unix = int(time.time())
            date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
 
            sensor = W1ThermSensor()
            
            temperature_in_fahrenheit = sensor.get_temperature(W1ThermSensor.DEGREES_F)         
       
            #print('Print jsonTest '  + str(jsonTest))
            #print('The temperature from new API is '+ str(temperature_in_fahrenheit))
            #print('This is the temp is all units' + str(temperature_in_all_units))

            tojson = json.dumps(temperature_in_fahrenheit)

            #insert a row of data into local db
            conn = sqlite3.connect('weatherdatabase.db')
            c = conn.cursor()
            c.execute('''INSERT INTO timetemp( time, temp )
                   VALUES(?,?)''', (date, temperature_in_fahrenheit))
            conn.commit()
            c.execute(""" select * from timetemp order by time asc limit 1 """)
            data = c.fetchall()
            conn.close()

            #return tojson + "  " + date
            return data
            
#gettemp_()             #for debugging
            
            
