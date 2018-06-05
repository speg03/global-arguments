import argparse


class CLIArgument(object):
    def __init__(self, key, help, **kwargs):
        self.key = key
        self.help = help
        self.kwargs = kwargs

        self.name = '--{}'.format(self.key.replace('_', '-'))

        if self.kwargs.get('default') is not None and \
           self.kwargs.get('type') is None:
            self.kwargs['type'] = type(self.kwargs['default'])


class CLIArgumentGroup(object):
    def __init__(self, name, *args):
        self.name = name
        self.args = args


class CLIArgumentExclusiveGroup(object):
    def __init__(self, *args, required=False):
        self.args = args
        self.required = required


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

        self._args = dict()
        self._groups = dict()

    def arg(self, key, help, **kwargs):
        return CLIArgument(key, help, **kwargs)

    def group(self, *args, name='Default'):
        return CLIArgumentGroup(name, *args)

    def exclusive(self, *args, required=False):
        return CLIArgumentExclusiveGroup(*args, required=required)

    def add_arguments(self, *args, target=None):
        target = target or self

        for arg in args:
            if isinstance(arg, CLIArgument):
                target.add_argument(arg.name, help=arg.help, **arg.kwargs)
                self._args[arg.key] = arg.kwargs.get('default')
            elif isinstance(arg, CLIArgumentGroup):
                arg_group = self._groups.get(arg.name)
                if arg_group is None:
                    arg_group = target.add_argument_group(arg.name)
                    self._groups[arg.name] = arg_group
                self.add_arguments(*arg.args, target=arg_group)
            elif isinstance(arg, CLIArgumentExclusiveGroup):
                ex_group = target.add_mutually_exclusive_group(
                    required=arg.required)
                self.add_arguments(*arg.args, target=ex_group)

    @property
    def default_args(self):
        return self._args


cli = CLIParser()
