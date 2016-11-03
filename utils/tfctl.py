#!/usr/local/bin/python2.7
# coding: utf-8

""" ctl for everything that can't be done without python """

from sys import argv
from json import dumps
from dictator import Dictator


def create():
    Dictator()[argv[2]] = argv[3:]


def error():
    raise ValueError(argv)


def dump():
    print dumps(Dictator().items(), indent=4, ensure_ascii=False)


def main():
    commands = {
        'create': create,
        'dump': dump,
    }

    assert argv[1] in commands, "Unknown command {0}".format(argv[1])
    commands.get(argv[1])()


if __name__ == '__main__':
    main()
