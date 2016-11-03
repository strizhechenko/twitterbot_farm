#!/usr/bin/env python2.7
# coding: utf-8

""" ctl for everything that can't be done without python """

from os import getenv
from sys import argv
from json import dumps
from dictator import Dictator
from twitterbot_farm import Reader, Writer

HOST = getenv('HOST', '127.0.0.1')


def create():
    Dictator(host=HOST)[argv[2]] = argv[3:]


def error():
    raise ValueError(argv)


def dump():
    print dumps(Dictator(host=HOST).items(), indent=4, ensure_ascii=False)


def stats():
    connect = Dictator(host=HOST)
    bots = [bot for bot in connect.keys() if bot != '__app__']
    for bot_name in bots:
        role = connect[bot_name][0]
        if role == 'reader':
            bot = Reader(bot_name.replace('@', ''), HOST)
            print "{0}={1}".format(bot_name, len(bot.connection.keys()))
        elif role == 'writer':
            bot = Writer(bot_name.replace('@', ''), HOST)
            print "{0}={1}".format(bot_name, len(bot.unprocessed_lines()))


def main():
    commands = {
        'create': create,
        'dump': dump,
        'stats': stats,
    }

    assert argv[1] in commands, "Unknown command {0}".format(argv[1])
    commands.get(argv[1])()


if __name__ == '__main__':
    main()
