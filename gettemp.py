import datetime
import hashlib
import pypyodbc
import sqlite3
import time
import random
from w1thermsensor import W1ThermSensor
from time import gmtime, strftime

#connect to DB
#conn = sqlite3.connect('weatherdatabase.db')
#c = conn.cursor()

#create 64bit hash for pi id
hash = hashlib.sha1("my message".encode("UTF-8")).hexdigest()
print(hash)
print(len(hash))


for sensor in W1ThermSensor.get_available_sensors():
    while True:
        #connect to dB's
#        connection = pypyodbc.connect('Driver={SQL Server};Server=weatherbuddy.ckvhavs0axwt.us-west-1.rds.amazonaws.com;Database=Weather;uid=snowboard;pwd=snowboard2000')
#        connection = pypyodbc.
#        cursor = connection.cursor()
        



        conn = sqlite3.connect('weatherdatabase.db')
        c = conn.cursor()
        far = sensor.get_temperature()*9/5 + 32 
        print("Sensor %s has temperature %.2f" % (sensor.id, sensor.get_temperature()))
        print(far)


        #insert a row of data into local db
        unix = int(time.time())
        date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
        keyword = 'Python'
#        value = random.randrage(0,10)

        c.execute('''INSERT INTO timetemp( time, temp )
                   VALUES(?,?)''', (date, far))


        #call stored proc to remote DB
#        cursor.execute('{EXEC [InsertTime](@temp=?, @time=?, @sig=?)}', (far,date,hash))



        #commit and close connection for local db
        conn.commit()
        time.sleep(2)
        conn.close()
        
print("all done")
