import sqlite3
import json

def getHistory():
  conn = sqlite3.connect('weatherdatabase.db')
  c = conn.cursor()


  c.execute(""" select * from timetemp """)
  data=c.fetchall()

  toJson = json.dumps(data)
  jsondumps2 = json.dumps(toJson)
  
  print('jsondumps2 ' + jsondumps2)

  #return toJson
  return data

getHistory()


