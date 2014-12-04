import pycurl
import urllib
import json
from config import BaseConfig
from StringIO import StringIO


class RequestManager():

    """docstring for RequestManager"""

    config = None
    request_url = ''

    def set_config(self, config):
        self.config = config

    def run(self):
        raise Exception("Proper implementation not set")


class MovieExtractionManager(RequestManager):

    """docstring for MovieExtractionManager"""

    def __init__(self):
        self.request_url = "http://api.rottentomatoes.com/api/public/"\
            "v1.0/lists/movies/opening.json"

    def run(self):
        buffer = StringIO()
        url_params = dict(
            apikey=BaseConfig.ROTTEN_TOMATO_APIKEY,
            limit=BaseConfig.RECORD_LIMIT
        )

        print(self.request_url
              + '?' + urllib.urlencode(url_params))
        c = pycurl.Curl()
        c.setopt(c.URL, self.request_url
                 + '?' + urllib.urlencode(url_params))
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()

        resp_string = buffer.getvalue()
        self.parse_and_store(resp_string)

    def parse_and_store(self, resp_string):
        parsed_data = self.parse_data(resp_string)
        self.store_data(parsed_data)

    def parsed_data(self, resp_string):
        parsed_data = []

        return parsed_data

    def store_data(self, data):
        pass
