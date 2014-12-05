from model import Model


class MoviesModel(Model):

    """docstring for MoviesModel"""
    table = 'movies'

    def __init__(self):
        Model.__init__(self)
