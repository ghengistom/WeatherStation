import sqlite3
import json

def getHistory():
  conn = sqlite3.connect('weatherdatabase.db')
  c = conn.cursor()


  c.execute(""" select * from timetemp """)
  data=c.fetchall()

  toJson = json.dumps(data)

  split1 = toJson.split(',')
  print(split1.split(',')) 
  
  #print(data)
  #return toJson
  return data

getHistory()      #for debugging


