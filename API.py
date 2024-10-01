import sqlite3

connection = sqlite3.connect("myDB.db")
cursor = connection.cursor()

# SQL CODE TO BE EXECUTED...

cursor.execute('''
CREATE TABLE table1(
    name VARCHAR(25),
    id NUMBER);
''')

connection.commit()
connection.close()

