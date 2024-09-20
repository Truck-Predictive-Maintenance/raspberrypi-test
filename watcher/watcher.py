import obd 
from obd import OBDResponse
import datetime

from db.controller import createLog

def watcher(obdResponse: OBDResponse):
    print("Watcher got the obdResponse")
    print(str(obdResponse))

    command = obdResponse.command
    response = obdResponse.value
    timestamp = datetime.datetime.fromtimestamp(obdResponse.time)
    raw = obdResponse.messages
    comment = ""

    createLog(command, response, comment,  timestamp, raw)
