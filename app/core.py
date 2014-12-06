from requests import MovieExtractionManager, MovieReviewManager


class ActionDispatcher():

    """docstring for ActionDispatcher"""
    runner = None

    def set_runner(self, runner):
        self.runner = runner


class Reviews(ActionDispatcher):
    """docstring for Movies"""
    is_booted = False

    def get_runner_config(self):
        pass

    def boot(self):
        movie_extractor = MovieReviewManager()
        self.set_runner(movie_extractor)
        self.runner.set_config(self.get_runner_config())
        self.is_booted = True

    def start(self):
        if not self.is_booted:
            self.boot()

        self.runner.run()


class Movies(ActionDispatcher):

    """docstring for Movies"""
    is_booted = False

    def get_runner_config(self):
        pass

    def boot(self):
        movie_extractor = MovieExtractionManager()
        self.set_runner(movie_extractor)
        self.runner.set_config(self.get_runner_config())
        self.is_booted = True

    def start(self):
        if not self.is_booted:
            self.boot()

        self.runner.run()
