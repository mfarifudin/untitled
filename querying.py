import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='tweets')
c = conn.cursor()

query = ("SELECT post FROM jokowi LIMIT 10")
c.execute(query)

for post in c:
    result = ''.join([i for i in post if not i.isdigit()])
    print(result)

c.close()
conn.close()