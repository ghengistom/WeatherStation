import sqlite3
conn = sqlite3.connect('weatherdatabase.db')
c = conn.cursor()


c.execute('SELECT * FROM timetemp)
#print(c.fetchall())   #print '"' + my_str + '"'
#print('"""' + mylist + '"""')

