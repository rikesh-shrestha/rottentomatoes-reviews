from os import path


class BaseConfig(object):
    STORAGE_PATH = path.abspath(
        path.join(
            path.dirname(path.dirname(__file__)),
            'storage'
        )
    )
    SQLITE_DB = path.join(STORAGE_PATH, 'review.db')
