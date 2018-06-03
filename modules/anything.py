from cli import cli

cli.arg('any', group='Runner', help='Any parameters', nargs='*')


class Runner(object):
    def __init__(self, **params):
        self._params = params

    def run(self):
        print(self._params)
