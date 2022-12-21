#!/usr/bin/python3
import argparse
from os import listdir

from commands.list_jobs import list_jobs
from commands.add_del_job import add_job, del_job
from commands.run_tracked import run_tracked, kill_job
from util import load_jobs

parser = argparse.ArgumentParser(prog='DfJobs')
subparsers = parser.add_subparsers(dest='subcommand')


def argument(*name_or_flags, **kwargs):
    return ([*name_or_flags], kwargs)


def subcommand(name, args=[], parent=subparsers):
    def decorator(func):
        parser = parent.add_parser(name)
        for arg, kwarg in args:
            parser.add_argument(*arg, **kwarg)
        parser.set_defaults(func=func)
    return decorator


@subcommand('help')
def help_command(args):
    parser.print_help()


@subcommand('add', [argument('name'), argument('path')])
def add_job_command(args):
    add_job(args.name, args.command)


@subcommand('del', [argument('name')])
def del_job_command(args):
    del_job(args.name)


@subcommand('run', [argument('name')])
def run_tracked_command(args):
    run_tracked(args.name)


@subcommand('startall')
def start_all_command(args):
    jobs = load_jobs()
    for name, job in jobs.items():
        if job.enabled:
            run_tracked(name)


@subcommand('killall')
def kill_all_command(args):
    for file in listdir('~/tools/dfjobs/jobs'):
        kill_job(file)


if __name__ == '__main__':
    args = parser.parse_args()
    if args.subcommand is None:
        list_jobs()
    else:
        args.func(args)