import sqlite3
import json

def getHistory():
  conn = sqlite3.connect('weatherdatabase.db')
  c = conn.cursor()

  c.execute(""" select time from timetemp """)
  data=c.fetchall()

  toJson = json.dumps(data)

  print('fetchall : ' + str(data))
  print('fetchall jsondumps' + toJson)
  #return toJson
  return data

getHistory()