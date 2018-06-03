from cli import cli

cli.arg('some', group='Runner', help='Some parameter', default=100, type=int)


class Runner(object):
    def __init__(self, **params):
        self._params = params

    def run(self):
        print(self._params)
