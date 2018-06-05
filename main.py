#!/usr/bin/env python3

from importlib import import_module

from cli import cli

cli.add_arguments(cli.arg('module', 'Module name for running', required=True))


def main():
    args, _ = cli.parse_known_args()

    module = import_module(args.module)

    args = cli.parse_args()
    if args.help:
        cli.print_help()
        exit()

    module.Runner(**vars(args)).run()


if __name__ == '__main__':
    main()
