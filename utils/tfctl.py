#!/usr/bin/env python2.7
# coding: utf-8

""" ctl for everything that can't be done without python """

from os import getenv
from sys import argv
from json import dumps
from requests import post
from dictator import Dictator
from twitterbot_farm import Reader, Writer

HOST = getenv('HOST', '127.0.0.1')
INFLUXDB_URL = getenv('INFLUXDB_URL', 'http://127.0.0.1:8086/write?db=twitterbot_farm')


def create():
    Dictator(host=HOST)[argv[2]] = argv[3:]


def error():
    raise ValueError(argv)


def dump():
    print dumps(Dictator(host=HOST).items(), indent=4, ensure_ascii=False)


def __stats__():
    connect = Dictator(host=HOST)
    bots = [bot.replace('@', '') for bot in connect.keys() if bot != '__app__']
    output = dict()
    for bot_name in bots:
        role = connect['@' + bot_name][0]
        if role == 'reader':
            output[bot_name] = len(Reader(bot_name, HOST).connection.keys())
        elif role == 'writer':
            output[bot_name] = len(Writer(bot_name, HOST).unprocessed_lines())
    return output


def stats():
    for bot_name, value in __stats__().items():
        print "{0}={1}".format(bot_name, value)


def send_stats():
    for bot_name, value in __stats__().items():
        data = "{0} value={1}".format(bot_name, value)
        print INFLUXDB_URL, '-d', data
        post(INFLUXDB_URL, data)


def main():
    commands = {
        'create': create,
        'dump': dump,
        'stats': stats,
        'send_stats': send_stats,
    }

    assert argv[1] in commands, "Unknown command {0}".format(argv[1])
    commands.get(argv[1])()


if __name__ == '__main__':
    main()
