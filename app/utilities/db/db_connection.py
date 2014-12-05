import sqlite3
from ..config import BaseConfig


def get_connection(args=None):
    connection = sqlite3.connect(aseConfig.SQLITE_DB)
    return connection
