from db_connection import connection


class Model():

    """docstring for Model"""
    db_connection = None
    table = ''

    def __init__(self):
        self.db_connection = connection

    def get(self, query=[]):
        pass

    def save(self, data=[], id=None):
        pass
