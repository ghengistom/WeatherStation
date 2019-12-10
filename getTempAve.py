import sqlite3
import json
import time
import datetime

def getTempAve():
  conn = sqlite3.connect('weatherdatabase.db')
  c = conn.cursor()
  #todays_date = datetime.datetime.now().date()

#SELECT CONVERT(date, getdate())

  #c.execute(" SELECT CONVERT(date, SELECT time from timetemp")
  c.execute("SELECT * FROM timetemp where temp like '%7%'")
  data=c.fetchall()
  conn.close()

  toJson = json.dumps(data)

  print(data)
  #return toJson
  return toJson

getTempAve()
#THis is the schema of the timetemp table
#   CREATE TABLE timetemp (
# time text PRIMARY KEY,
# temp float NOT NULL
# );