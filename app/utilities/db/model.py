from db_connection import db_connection


class Model():

    """docstring for Model"""
    db_connection = None
    table = ''
    primary_key = ''

    def __init__(self):
        self.db_connection = db_connection

    def set_table(self, table):
        self.table = table

    def get(self, filters={}):
        query = self.prep_get_query(filters)
        self.db_connection.get().execute(query)
        return self.db_connection.get().fetchall()

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
        query = "INSERT INTO {0:s} ('{1:s}', {2:s}) "\
            "VALUES (NULL, {3:s})" . format(
                self.table,
                self.primary_key,
                '"' + '", "'.join(params.keys()) + '"',
                '"' + '", "'.join(params.values()) + '"'
            )
        return query

    def prep_get_query(self, filters):
        query = ""
        _select = "*"
        _where = ""

        if 'select' in filters:
            _select = ""
            for key, value in filters['select']:
                _select += " {0:s} = '{1:s}'" . format(key, value)

        if 'where' in filters:
            for value in filters['where']:
                _where += " {0:s} {1:s} '{2:s}'".format(*value)

            _where = " WHERE" + _where

        query = "SELECT {0:s} FROM {1:s}{2:s}" . format(
            _select,
            self.table,
            _where
        )

        return query
