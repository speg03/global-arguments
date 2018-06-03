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

        self._args = dict()
        self._groups = dict()
        self._exclusive_groups = dict()

    def arg(self, key, group=None, exclusive=None, required=False, **kwargs):
        if group is None:
            target = self
        else:
            arg_group = self._groups.get(group)
            if arg_group is None:
                arg_group = self.add_argument_group(group)
                self._groups[group] = arg_group

            target = arg_group

        if exclusive is None:
            target.add_argument(
                '--{}'.format(key), required=required, **kwargs)
        else:
            ex_group = self._exclusive_groups.get(exclusive)
            if ex_group is None:
                ex_group = target.add_mutually_exclusive_group(
                    required=required)
                self._exclusive_groups[exclusive] = ex_group

            ex_group.add_argument('--{}'.format(key), **kwargs)

        self._args[key] = kwargs.get('default')

    @property
    def default_args(self):
        return self._args


cli = CLIParser()
