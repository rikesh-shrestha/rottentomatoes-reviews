import pycurl
import urllib
import json
import re
import urlparse
from config import BaseConfig
from StringIO import StringIO
import utilities.db.models as models

movie_m = models.MoviesModel()
review_m = models.ReviewModel()
log_m = models.ExtractionLogModel()
pagenumber_pattern = re.compile("(?<=\Wpage\=)\d+")


class RequestManager():

    """docstring for RequestManager"""

    config = None
    request_url = ''
    counter = 0

    def increase_counter(self):
        self.counter += 1
        return self.counter

    def set_config(self, config):
        self.config = config

    def make_request(self, params):
        pass

    def run(self):
        raise Exception("Proper implementation not set")


class MovieReviewManager(RequestManager):

    """docstring for MovieReviewManager"""

    def __init__(self):
        self.request_url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/{0}/reviews.json'

    def make_request(self, movie_id, url_params):
        buffer = StringIO()
        url = self.request_url.format(movie_id)
        url += '?' + urllib.urlencode(url_params)
        c = pycurl.Curl()

        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        return buffer.getvalue()

    def get_eligible_movies(self):
        return movie_m.get()

    def get_movie_reviews(self, movie_id):
        page_number = 1
        request_param = dict(
            apikey=BaseConfig.ROTTEN_TOMATO_APIKEY,
            limit=BaseConfig.RECORD_LIMIT,
            review_type='all'
        )
        moview_counter = 0

        while page_number is not None:
            last_page = page_number
            request_param['page'] = page_number
            response_string = self.make_request(movie_id, request_param)
            parsed_data = json.loads(response_string)
            self.store_data(movie_id, parsed_data)
            page_number = self.get_next_page(parsed_data)
            moview_counter += len(parsed_data['reviews'])

        log_m.set_movie_log('movie-count', moview_counter, movie_id)
        log_m.set_movie_log('log-page-number', last_page, movie_id)

    def store_data(self, movie_id, parsed_data):
        for review in parsed_data['reviews']:
            db_dump = {
                "rated_at": review['date'],
                'freshness': review['freshness'],
                'review_text': re.sub(r'"', '\'', review['quote']),
                'rt_moview_id': str(movie_id)
            }
            review_m.save(db_dump)
            print "{0} Reviews collected".format(self.increase_counter())

    def run(self):
        for movie in self.get_eligible_movies():
            self.get_movie_reviews(movie['rt_moview_id'])

    def get_next_page(self, parsed_data):
        page = None
        if 'next' in parsed_data['links']:
            next_link = parsed_data['links']['next']
            page = pagenumber_pattern.search(next_link)
            page = page.group(0) if page is not None else page

        return page


class MovieExtractionManager(RequestManager):

    """docstring for MovieExtractionManager"""

    def __init__(self):
        self.request_url = "http://api.rottentomatoes.com/api/public/"\
            "v1.0/lists/movies/in_theaters.json"

    def make_request(self, url):
        buffer = StringIO()
        c = pycurl.Curl()

        c.setopt(c.URL, url)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        return buffer.getvalue()

    def run(self):
        url_params = dict(
            apikey=BaseConfig.ROTTEN_TOMATO_APIKEY,
            limit=BaseConfig.RECORD_LIMIT
        )
        url_to_use = self.request_url + '?' + urllib.urlencode(url_params)

        resp_string = self.make_request(url_to_use)
        self.parse_and_store(resp_string)

    def parse_and_store(self, resp_string):
        data = json.loads(resp_string)
        for movie in data['movies']:
            db_dump = {
                'movie_name': movie['title'],
                'rt_moview_id': movie['id'],
                'release_date': movie['release_dates']['theater']
            }
            movie_m.save(db_dump)

        if 'next' in data['links']:
            print data['links']['next']

    def store_data(self, data):
        pass
