import sqlite3
import json

def getHistory():
  conn = sqlite3.connect('weatherdatabase.db')
  c = conn.cursor()


  c.execute(""" select * from timetemp """)
  data=c.fetchall()

  toJson = json.dumps(data)
  print(toJson)

  return toJson

# for i,j in data:
#     print(i)
#     print(j)

# for i in toJson:
#     print(i)
  

#print(data)

#c.execute('SELECT * FROM timetemp)
#print(c.fetchall())   #print '"' + my_str + '"'
#print('"""' + mylist + '"""')

