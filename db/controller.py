from peewee import *
from db.connection import get_db
from db.model import ObdLog 
import logging

def createLog(command, response, comment, timestamp, raw):
    logger = logging.getLogger('obd-logger')
    logger.debug(f'Adding log to db: command {command} | response {response} | comment {comment} | timestamp {timestamp} | raw {raw}')

    newLog = ObdLog.create(
        timestamp = timestamp,
        command = command,
        response = response,
        comment = comment,
        raw = raw
    )