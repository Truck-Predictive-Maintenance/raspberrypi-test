import sqlite3
from typing import Generator
from peewee import *

def get_db():
    return  SqliteDatabase('obdlog_database.db')

