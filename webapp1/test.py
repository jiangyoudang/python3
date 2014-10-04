# import mysql.connector
#
# config = {'user':'root', 'password':'a11', 'database':'test','host':'127.0.0.1', 'port':'3306'}
#
# conn = mysql.connector.connect(**config)
# cursor = conn.cursor()
# # cursor.execute('insert into user (id, name) values (%s,%s)', (5,'c5'))
#
# conn.commit()
#
#
# print(cursor)
# for i in cursor:
#     print(i)
#
#
# conn.close()
# a, b = zip(*config.items())
#
# s = ['safe']
# s.append('APPEND')
# print(s)

import logging
logging.basicConfig(level=logging.DEBUG, format='%(module)s-%(levelname)s:  %(message)s')


from webapp1.model import User
from webapp1.lib import db

db.create_engine('root','a11', 'test')
u = User(id=1, name='cong_test', email='test@test.com')

# print(u.sql())
# u.insert()

r = User.find_one('id=?',1)
print(r)