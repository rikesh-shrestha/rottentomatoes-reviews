import sqlite3
from ...config import BaseConfig


class DbConnections():

    def __init__(self):
        self.connection = sqlite3.connect(BaseConfig.SQLITE_DB)
        self.c = self.connection.cursor()

    def get(self):
        return self.c

    def commit(self):
        self.connection.commit()

db_connection = DbConnections()
