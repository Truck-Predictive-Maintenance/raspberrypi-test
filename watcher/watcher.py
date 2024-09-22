from obd import OBDResponse
import datetime

from db.controller import createLog
import logging

def watcher(obdResponse: OBDResponse):
    logger = logging.getLogger('obd-logger')
    logger.debug(f'watcher got response: {obdResponse}')

    command = obdResponse.command
    response = obdResponse.value
    timestamp = datetime.datetime.fromtimestamp(obdResponse.time)
    raw = obdResponse.messages
    comment = ""

    createLog(command, response, comment,  timestamp, raw)
