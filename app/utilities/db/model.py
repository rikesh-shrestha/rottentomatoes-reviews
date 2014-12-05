from db_connection import db_connection


class Model():

    """docstring for Model"""
    db_connection = None
    table = ''

    def __init__(self):
        self.db_connection = db_connection

    def set_table(self, table):
        self.table = table

    def get(self, query=[]):
        pass

    def save(self, data, id=None):
        query = ""
        if id is None:
            query = self.prep_insert_query(data)
        else:
            query = self.prep_update_query(id, data)

        self.db_connection.get().execute(query)
        return self.db_connection.commit()

    def prep_update_query(self, id, params):
        query = ""
        return query

    def prep_insert_query(self, params):
        query = ""
        query = "INSERT INTO {0:s} ('id', {1:s}) VALUES (NULL, {2:s})" . format(
            self.table,
            "'" + "', '".join(params.keys()) + "'",
            "'" + "', '".join(params.values()) + "'"
        )
        return query

    def prep_get_query(self, filters):
        pass
