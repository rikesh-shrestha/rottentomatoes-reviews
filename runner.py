import sys
from app import RottenTomato, config


def get_movies():
    return RottenTomato.Movies()


def get_reviews():
    print 'we are working to get reviews'


def get_action_dispatcher(action):
    if action == 'movies':
        return get_movies()

    else:
        raise Exception("Proper action not found")


def main():
    action = 'default' if (len(sys.argv) < 2) else sys.argv[1]
    action_dispatcher = get_action_dispatcher(action)

    try:
        action_dispatcher.start()
    except Exception, e:
        raise e
    else:
        pass

if __name__ == '__main__':
    main()
