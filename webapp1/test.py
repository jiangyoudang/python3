import mysql.connector

config = {'user':'root', 'password':'a11', 'database':'test','host':'127.0.0.1', 'port':'3306'}

conn = mysql.connector.connect(**config)
cursor = conn.cursor()
cursor.execute('select * from user')


print(cursor.description)
for i in cursor:
    print(i)



a, b = zip(*config.items())


