from peewee import *
from db.connection import get_db
from db.model import ObdLog 

def createLog(command, response, comment, timestamp, raw):
    newLog = ObdLog.create(
        timestamp = timestamp,
        command = command,
        response = response,
        comment = comment,
        raw = raw
    )

    print("Added new Log")