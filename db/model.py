from peewee import *
import datetime

db =  SqliteDatabase('obdlog_database.db')

class BaseModel(Model):
    class Meta: 
        database = db

class ObdLog(BaseModel):
    timestamp = DateTimeField(default = datetime.datetime.now)
    command = TextField()
    response = TextField()
    comment = TextField()
    raw = TextField()
    isSent = BooleanField(default = False)