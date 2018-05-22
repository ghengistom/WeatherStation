import sqlite3
import json

def getHistory():
  conn = sqlite3.connect('weatherdatabase.db')
  c = conn.cursor()

  c.execute(""" select * from timetemp """)
  data=c.fetchall()

  toJson = json.dumps(data)

  getone = toJson[21]
  print('contents of getone' + getone)
  #print(data)
  #return toJson
  return data

getHistory()      #for debugging


