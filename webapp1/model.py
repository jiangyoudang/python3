
import time

from .lib.orm import Model, StringField, BooleanField, FloatField

class User(Model):

    id = StringField(primary_key=True)
    email = StringField()
    name = StringField()
    admin = BooleanField()
    create_at = FloatField(updatable=False, default=time.time())

