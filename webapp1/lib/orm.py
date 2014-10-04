import logging

from webapp1.lib import db

class Field(object):

    _count = 0

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self._default = kwargs.get('default', None)
        self.primary_key = kwargs.get('primary_key', None)
        self.nullable = kwargs.get('nullable', False)
        self.updatable = kwargs.get('updatable', True)
        self.insertable = kwargs.get('insertable', True)
        self.ddl = kwargs.get('ddl', '')
        self._order = Field._count
        Field._count = Field._count + 1

    @property
    def default(self):
        d = self._default
        return d() if callable(d) else d

    def __str__(self):
        s = ['<{}, {}:{}, default:{}'.format(self.name, self.__class__.__name__, self.ddl, self._default)]
        self.nullable and s.append('N')
        self.updatable and s.append('U')
        self.insertable and s.append('I')
        s.append('>')
        return ''.join(s)

class StringField(Field):

    def __init__(self, **kwargs):
        if not 'default' in kwargs:
            kwargs['default'] = ''
        if not 'ddl' in kwargs:
            kwargs['ddl'] = 'varchar(255)'
        super().__init__(**kwargs)

class IntegerField(Field):

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = 0
        if not 'ddl' in kw:
            kw['ddl'] = 'bigint'
        super().__init__(**kw)

class FloatField(Field):

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = 0.0
        if not 'ddl' in kw:
            kw['ddl'] = 'real'
        super().__init__(**kw)

class BooleanField(Field):

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = False
        if not 'ddl' in kw:
            kw['ddl'] = 'bool'
        super().__init__(**kw)

class TextField(Field):

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = ''
        if not 'ddl' in kw:
            kw['ddl'] = 'text'
        super().__init__(**kw)

class BlobField(Field):

    def __init__(self, **kw):
        if not 'default' in kw:
            kw['default'] = ''
        if not 'ddl' in kw:
            kw['ddl'] = 'blob'
        super().__init__(**kw)

class VersionField(Field):

    def __init__(self, name=None):
        super().__init__(name=name, default=0, ddl='bigint')

def _gen_sql(table_name, mapping):
    pk = None
    sql = ['--generating sql for {}:'.format(table_name)]
    sql.append('create table {} ('.format(table_name))
    for k, v in mapping.items():
        if not hasattr(v, 'ddl'):
            raise TypeError('{} Field has no ddl'.format(v))
        if v.primary_key:
            pk = v.name
        if v.nullable:
            sql.append('  `{}` {},'.format(v.name, v.ddl))
        else:
            sql.append('  `{}` {} not null,'.format(v.name, v.ddl))
    sql.append('  primary key(`{}`)'.format(pk))
    sql.append(');')
    return '\n'.join(sql)

class ModelMetaClass(type):

    def __new__(cls, name, base, dct):

        if name=='Model':
            return type.__new__(cls, name, base, dct)

        if not hasattr(cls, 'subclass'):
            cls.subclass = {}
        if not name in cls.subclass:
            cls.subclass[name] = name
        else:
            logging.warning('redefine class {}'.format(name))


        logging.info('scan orm mapping {}'.format(name))
        mapping = dict()
        primary_key = None
        for k, v in dct.items():
            if isinstance(v, Field):
                if not v.name:
                    v.name = k
                logging.info('mapping {}:{}'.format(k, v))

                if v.primary_key:
                    if primary_key:
                        raise TypeError('more than 1 primary key defined in {}'.format(name))
                    if v.updatable:
                        logging.warning('NOTE: changing primary key to non-updatable')
                        v.updatable = False
                    if v.nullable:
                        logging.warning('NOTE: changing primary key to non-nullalbe')
                        v.nullable = False

                    primary_key = v.name
                mapping[k] = v

        if not primary_key:
            raise TypeError('primary key not defined in {}'.format(name))
        for k in mapping.keys():
            dct.pop(k)
        if not '__table__' in dct:
            dct['__table__'] = name.lower()

        dct['__mapping__'] = mapping
        dct['__primary_key__'] = primary_key
        dct['sql'] = lambda self: _gen_sql(dct['__table__'], mapping)

        return type.__new__(cls, name, base, dct)





class Model(dict, metaclass = ModelMetaClass):

    # __metaclass__ = ModelMetaClass

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError('attribute {} not exist'.format(item))

    def __setattr__(self, key, value):
        self[key] = value

    @classmethod
    def get(cls, pk):
        d = db.select_one('select * from {} where {}=?'.format(cls.__table__, cls.__primary_key__), pk)
        return cls(**d) if d else None

    @classmethod
    def find_one(cls, where, *args):
        d = db.select_one('select * from {} where {}'.format(cls.__table__, where), *args)
        return cls(**d) if d else None

    @classmethod
    def find_all(cls, where, *args):
        dl = db.select('select * from {} where {}'.format(cls.__table__, where), *args)
        return [cls(**d) for d in dl]

    @classmethod
    def find(cls, sql, *args):
        '''
         find by sql clause
        :param sql:
        :param args:
        :return:
        '''
        r = db.select(sql, *args)
        if isinstance(r, list):
            return [cls(**d) for d in r]
        elif isinstance(r, dict):
            return cls(**r) if r else None


    def insert(self):
        table = self.__table__
        params = dict()
        for k, v in self.__mapping__.items():
            if v.insertable:
                if not hasattr(self, k):
                    setattr(self, k, v._default)
                params[v.name] = getattr(self, k)
        db.insert(table, **params)
        return self


if __name__=='__main__':
    logging.basicConfig(level=logging.DEBUG)
    db.create_engine('root', 'a11', 'test')
    db.update('drop table if exists user')
    # db.update('create table user (id int primary key, name text, email text, passwd text, last_modified real)')

