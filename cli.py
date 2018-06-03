import argparse


class CLIParser(argparse.ArgumentParser):
    def __init__(self):
        super().__init__(
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.add_argument(
            '-h',
            '--help',
            action='store_true',
            help='show this help message and exit')

    def arg(self, key, **kwargs):
        self.add_argument('--{}'.format(key), **kwargs)


cli = CLIParser()
