__author__ = 'congliu'

import sqlite3
db_filename = 'data.db'
schema_filename = 'schema.sql'


# create new table
def create_table():
    with sqlite3.connect('data.db') as conn:
        print('Creating schema')
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        print('Inserting initial data')

        conn.execute("""
        insert into users(name, description, email)
        values ('cong', 'Hello World', 'cliu1@scu.edu')
        """)



def get_user():
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        cursor.execute("""select * from users""")
        id, name, description, email =cursor.fetchone()
        d = {'id':id, 'description': description, 'name':name, 'email':email}
        return d


