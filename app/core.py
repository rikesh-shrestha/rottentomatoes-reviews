from requests import RequestManager


class ActionDispatcher():

    """docstring for ActionDispatcher"""

    def start(self):
        raise Exception("Implementation for action handler not set")


class Movies(ActionDispatcher):

    """docstring for Movies"""
    is_booted = False

    def boot(self):
        self.is_booted = True

    def start(self):
        print 'starting'
