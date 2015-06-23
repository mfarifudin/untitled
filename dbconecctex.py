__author__ = 'Muh Fatkhan Arifudin'
import mysql.connector
import datetime


#        replace mysql.server with "localhost" if you are running via your own server!
#                        server       MySQL username	MySQL pass  Database name.
conn = mysql.connector.connect(user='root', password='', host='127.0.0.1',database='tweets')

c = conn.cursor()

c.execute("INSERT INTO tweets (time, username, post) VALUES (%s,%s,%s)", (time.time(), username, tweet))

conn.commit()

c.execute("SELECT * FROM tweets")

rows = c.fetchall()

for eachRow in rows:
    print(eachRow)