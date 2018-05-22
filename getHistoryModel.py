import sqlite3
import json

def getHistory():
  conn = sqlite3.connect('weatherdatabase.db')
  c = conn.cursor()


  c.execute(""" select * from timetemp """)
  data=c.fetchall()

  toJson = json.dumps(data)
  toJson2 = json.loads(toJson)
  print('jsonloads ' + toJson2)

  #return toJson
  return data

getHistory()


