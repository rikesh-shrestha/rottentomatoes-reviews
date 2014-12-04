from os import path


class BaseConfig(object):
    STORAGE_PATH = path.abspath(
        path.join(
            path.dirname(path.dirname(__file__)),
            'storage'
        )
    )
    SQLITE_DB = path.join(STORAGE_PATH, 'review.db')
    ROTTEN_TOMATO_APIKEY = "9pttf673jh8byc3z6qryaxy9"
    RECORD_LIMIT = 20
