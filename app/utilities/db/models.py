from model import Model


class MoviesModel(Model):

    """docstring for MoviesModel"""
    table = 'movies'
    primary_key = 'id'

    def __init__(self):
        Model.__init__(self)


class ReviewModel(Model):

    """docstring for ReviewModel"""
    table = 'reviews'
    primary_key = 'id'

    def __init__(self):
        Model.__init__(self)


class ExtractionLogModel(Model):

    """docstring for ReviewModel"""
    table = 'extraction_log'
    primary_key = 'id'

    def __init__(self):
        Model.__init__(self)

    def set_log(self, log_origin, log_key, log_value, log_meta=None):
        db_dump = dict(
            log_origin=str(log_origin),
            log_key=str(log_key),
            log_val=str(log_value)
        )

        if log_meta is not None:
            db_dump['log_meta'] = str(log_meta)

        return self.save(db_dump)

    def set_movie_log(self, log_key, log_value, log_meta=None):
        return self.set_log(
            'movie',
            log_key,
            log_value,
            log_meta
        )
