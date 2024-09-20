from peewee import *
import datetime

from db.connection import get_db 

class BaseModel(Model):
    class Meta: 
        database = get_db()

class ObdLog(BaseModel):
    timestamp = DateTimeField(default = datetime.datetime.now)
    command = TextField()
    response = TextField()
    comment = TextField()
    raw = TextField()
    isSent = BooleanField(default = False)