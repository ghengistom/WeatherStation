import sqlite3
conn = sqlite3.connect('weatherdatabase.db')
c = conn.cursor()


c.execute(""" select * from timetemp """)
data=c.fetchall()

for i,j in data:
    print(i)
    print(j)

#print(data)

#c.execute('SELECT * FROM timetemp)
#print(c.fetchall())   #print '"' + my_str + '"'
#print('"""' + mylist + '"""')

