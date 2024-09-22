import obd
from peewee import *

from db.connection import get_db
from db.model import ObdLog
from watcher.watcher import watcher

import logging

device_addr = "4c:6b:e8:c5:fe:58"
rfcomm_channel = 2

def main():
    # initialize DB Tables
    db = get_db()
    db.connect()
    db.create_tables([ObdLog])

    # init logger
    logging.basicConfig(level=logging.DEBUG, filename="OBD_LOGGER.log")
    logger = logging.getLogger('obd-logger')
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s  -  %(levelname)s  -  %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.debug('##### OBD Logger Program STARTED ##### ')

    try:
        connection = obd.Async()
        connection.watch(obd.commands.SPEED, callback=watcher)
        connection.watch(obd.commands.RPM, callback=watcher)
        connection.start()

        while True:
            pass 

    except OSError as e:
        logger.error("Error occured during OBD Logging Service...")
    finally:
        connection.stop()
        logger.debug('##### OBD Logger Program TERMINATED ##### ')

if __name__ == "__main__":
    main()