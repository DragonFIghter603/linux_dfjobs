import sys
import argparse

from commands.list_jobs import list_jobs
from commands.add_job import add_job

parser = argparse.ArgumentParser(prog='DfJobs')
subparsers = parser.add_subparsers(dest='subcommand')


def argument(*name_or_flags, **kwargs):
    return ([*name_or_flags], kwargs)


def subcommand(name, args=[], parent=subparsers):
    def decorator(func):
        print(func)
        parser = parent.add_parser(name)
        for arg, kwarg in args:
            parser.add_argument(*arg, **kwarg)
        parser.set_defaults(func=func)
    return decorator


@subcommand('help', [])
def add_job(args):
    parser.print_help()


@subcommand('add', [argument('name'), argument('path')])
def add_job(args):
    add_job(args.name, args.path)


@subcommand('del', [argument('name')])
def del_job(args):
    del_job(args.name, args.path)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.subcommand is None:
        list_jobs()
    else:
        args.func(args)