from cli import cli

cli.add_arguments(
    cli.group(cli.arg('any', 'Any parameters', nargs='*'), name='Runner'))


class Runner(object):
    def __init__(self, **params):
        self._params = {**cli.default_args, **params}

    def run(self):
        print(self._params)
