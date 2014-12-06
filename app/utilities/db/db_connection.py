import sqlite3
from ...config import BaseConfig


class DbConnections():

    def __init__(self):
        self.connection = sqlite3.connect(BaseConfig.SQLITE_DB)
        self.connection.row_factory = self.dict_factory
        self.c = self.connection.cursor()

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get(self):
        return self.c

    def commit(self):
        self.connection.commit()

db_connection = DbConnections()
