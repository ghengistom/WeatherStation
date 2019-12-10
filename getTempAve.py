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
  #c.execute("SELECT * FROM timetemp where temp like '%7%'")

  dt = datetime.datetime.now().date()
  print(dt)

  #c.execute("Select CAST(time as date), AVG(temp) From timetemp Group By CAST(time as date)")
  c.execute("SELECT *, AVG(temp) FROM timetemp where time like 'dt' GROUP BY CAST(time as date)")
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