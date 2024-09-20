import obd
from peewee import *
import time

from db.connection import get_db
from db.model import ObdLog
from watcher.watcher import watcher

device_addr = "4c:6b:e8:c5:fe:58"
rfcomm_channel = 1

def main():
    # initialize DB Tables
    db = get_db()
    print(db)
    db.connect()
    db.create_tables([ObdLog])

    connection = obd.Async()
    connection.watch(obd.commands.SPEED, callback=watcher)
    connection.watch(obd.commands.RPM, callback=watcher)

    connection.start()

    time.sleep(30)
    connection.stop()

if __name__ == "__main__":
    main()