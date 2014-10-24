import logging, threading, functools
import mysql.connector

from Dict import Dict

class DBError(Exception):
    pass


class _Engine(object):
    def __init__(self, connection):
        self._connection = connection

    def connection(self):
        return self._connection()

#global
engine = None

def create_engine(usr, psw, database, host='127.0.0.1', port=3306, **kwargs):
    import mysql.connector
    global engine
    if engine is not None:
        raise DBError('engine is already exist')
    params = dict(user=usr, password=psw, database=database, host=host, port=port)
    defaults = dict(use_unicode=True, charset='utf8', collation='utf8_general_ci', autocommit=False)
    for k, v in defaults.items():
        params[k] = kwargs.pop(k, v)
    params.update(kwargs)
    params['buffered'] = True
    engine = _Engine(lambda: mysql.connector.connect(**params))
    # test connection...
    logging.info('Init mysql engine <{}> ok.'.format( hex(id(engine))))

class _LazyConnection(object):
    def __init__(self):
        self.connection = None

    def cursor(self):
        if self.connection is None:
            connection = engine.connection()
            logging.info('open connection {}'.format(hex(id(connection))))
            self.connection = connection

        return self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def cleanup(self):
        if self.connection:
            connection = self.connection
            self.connection = None
            logging.info('close connection {}'.format(hex(id(connection))))
            connection.close()

class _Db_local(threading.local):

    def __init__(self):
        self.connection = None
        self.transitions = 0

    def is_init(self):
        return not self.connection is None

    def init(self):
        logging.info('open lazy connection...')
        self.connection = _LazyConnection()
        self.transitions = 0

    def cleanup(self):
        self.connection.cleanup()
        self.connection = None

#global
_dbcnx = _Db_local()

class _Connection(object):
    def __enter__(self):
        global _dbcnx
        self.should_clean = False
        if not _dbcnx.is_init():
            _dbcnx.init()
            self.should_clean = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        global _dbcnx
        if self.should_clean:
            _dbcnx.cleanup()

def connection():
    return _Connection()


def with_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with _Connection():
            return func(*args, **kwargs)

    return wrapper


def _select(sql, one, *args):
    global _dbcnx
    cursor = None
    sql = sql.replace('?', '%s')
    logging.info('sql: {}, args: {}'.format(sql, args))

    try:
        cursor = _dbcnx.connection.cursor()
        cursor.execute(sql, args)
        col_name = None
        if cursor.description:
            col_name = [i[0] for i in cursor.description]

        if one:
            value = cursor.fetchone()
            if not value:
                return None

            return Dict(col_name, value)
        return [Dict(col_name, value) for value in cursor.fetchall()]

    finally:
        if cursor:
            cursor.close()


@with_connection
def select_one(sql, *args):
    return _select(sql, True, *args)


@with_connection
def select(sql, *args):
    return _select(sql, False, *args)

@with_connection
def _update(sql, *args):
    global _dbcnx
    cursor = None
    sql = sql.replace('?', '%s')
    logging.info('sql: {}, args: {}'.format(sql, args))
    print(sql)
    print(args)


    try:
        cursor = _dbcnx.connection.cursor()
        cursor.execute(sql, args)
        _dbcnx.connection.commit()
    # except:
    #     _dbcnx.connection.rollback()
    #     raise
    finally:
        if cursor:
            cursor.close()



def insert(table, **kwargs):
    col, value = zip(*kwargs.items())
    sql = 'insert into `{}`({}) values ({})'.format(
                                            table ,
                                            ','.join(['{}'.format(i) for i in col]),
                                            ','.join(['?' for i in value]))

    return _update(sql, *value)

def update(sql, *args):
    return _update(sql, *args)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    create_engine('root', 'a11', 'test')
    update('drop table if exists user')
    update('create table user (id int primary key, name text, email text, passwd text, last_modified real)')
    # with connection():
    insert('user', id=4, name = 'test4')