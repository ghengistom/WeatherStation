import sqlite3
conn = sqlite3.connect('weatherdatabase.db')
c = conn.cursor()


mylist = c.execute('SELECT * FROM timetemp)
print(c.fetchall())