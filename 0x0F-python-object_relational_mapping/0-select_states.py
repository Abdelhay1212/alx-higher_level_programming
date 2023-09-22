#!/usr/bin/python3
import sys
import MySQLdb


userName = sys.argv[2]
password = sys.argv[3]
mydb = sys.argv[4]

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
