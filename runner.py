import sys
from app import RottenTomato, config
import app.utilities.db.models as models


def get_movies():
    return RottenTomato.Movies()


def get_reviews():
    print 'we are working to get reviews'


def get_action_dispatcher(action):
    if action == 'movies':
        return get_movies()
    else:
        raise Exception("Proper action not found")


def get_tests():
    movies = models.MoviesModel()
    db_data = dict(
        name="Penguins of Madagascar",
        rt_movie_id="12121",
        release_date="afadfadf",
        freshness="fadfadf"
    )
    movies.save(db_data)


def main():
    action = 'default' if (len(sys.argv) < 2) else sys.argv[1]

    if action == 'test':
        get_tests()
    else:
        action_dispatcher = get_action_dispatcher(action)

        try:
            action_dispatcher.start()
        except Exception, e:
            raise e
        else:
            pass

if __name__ == '__main__':
    main()
