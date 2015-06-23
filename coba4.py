__author__ = 'Muh Fatkhan Arifudin'
import json
import mysql.connector
import time

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1',database='tweets')
c = conn.cursor()

tweet = []
post = []

for line in open('tweets4.txt', 'r'):
    tweet.append(json.loads(line))

print(tweet.__getitem__('text'))
'''
c.execute("INSERT INTO tweets (time, username, post) VALUES (%s,%s,%s)",
        (time.time(), username, post))

conn.commit()
'''
