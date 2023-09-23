#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb


userName = sys.argv[1]
password = sys.argv[2]
mydb = sys.argv[3]

connection = MySQLdb.connect(
    host='localhost',
    user=userName,
    passwd=password,
    db=mydb
)

cursor = connection.cursor()
cursor.execute('SELECT * FROM states')
result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
connection.close()
