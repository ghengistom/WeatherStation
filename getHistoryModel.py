import sqlite3
conn = sqlite3.connect('weatherdatabase.db')
c = conn.cursor()


mylist = ''.join(c.execute('SELECT * FROM timetemp))
print(c.fetchall())