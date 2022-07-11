#!/usr/bin/env python

from email.policy import default
import click
from package.taskily import TaskList
import hashlib
from datetime import date, datetime
from pathlib import Path
import pickle

def _get_path() -> Path:
    hsh = hashlib.sha256()
    hsh.update(str(datetime.today().strftime('%Y-%m-%d')).encode('UTF-8'))
    home = Path.home()
    (home/'.cache'/'taskily'/f'{hsh.hexdigest()[:10]}.pkl').parent.mkdir(exist_ok=True, parents=True)
    return home/'.cache'/'taskily'/f'{hsh.hexdigest()[:10]}.pkl'

def _get_list() -> TaskList:
    with open(str(_get_path()), "rb") as input_file:
        return pickle.load(input_file)

def _write_list(tl) -> None:
    with open(str(_get_path()), "wb") as output_file:
        pickle.dump(tl, output_file)

def _finish(tl) -> None:
    _write_list(tl)
    click.echo(str(tl))

@click.group(invoke_without_command=True)
def main():
    pass

@main.command('list')
def list():
    _finish(_get_list())

@main.command('init')
@click.option('--start_hour', '-sh', type=int, help='Starting Hour', default=7)
@click.option('--start_minute', '-sm', type=int, help='Starting Hour', default=0)
def init(start_hour, start_minute):
    _finish(TaskList(datetime(1, 1, 1, start_hour, start_minute)))


@main.command('append')
@click.option('--name', '-n', required=True, type=str, help='Name of the Task')
@click.option('--duration', '-d', required=True, type=int, help='Duration of Task, in Minutes')
def append(name, duration):
    tl = _get_list()
    tl.append(name, duration)
    _finish(tl)

@main.command('insert')
@click.option('--name', '-n', required=True, type=str, help='Name of the Task')
@click.option('--duration', '-d', required=True, type=int, help='Duration of Task, in Minutes')
@click.option('--index', '-i', type=int, help='Index to Insert At', default=1)
def append(name, duration, index):
    tl = _get_list()
    tl.insert(name, duration, index-1)
    _finish(tl)

@main.command('sinsert')
@click.option('--name', '-n', required=True, type=str, help='Name of the Task')
@click.option('--duration', '-d', required=True, type=int, help='Duration of Task, in Minutes')
@click.option('--time', '-t', required=True, type=int, help='Time to Split Task at, in Minutes')
@click.option('--index', '-i', type=int, help='Index to Splice At', default=1)
def append(name, duration, time, index):
    tl = _get_list()
    tl.insert_splice(name, duration, time, index-1)
    _finish(tl)

@main.command('remove')
@click.option('--index', '-i', required=True, type=int, help='Index to Remove')
def append(index):
    tl = _get_list()
    tl.remove(index-1)
    _finish(tl)

@main.command('replace')
@click.option('--name', '-n', required=True, type=str, help='Name of the Task')
@click.option('--duration', '-d', required=True, type=int, help='Duration of Task, in Minutes')
@click.option('--index', '-i', type=int, help='Index to Replace At', default=1)
def append(name, duration, index):
    tl = _get_list()
    tl.replace(name, duration, index-1)
    _finish(tl)


if __name__ == '__main__':
    main()