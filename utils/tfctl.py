#!/usr/bin/env python2.7
# coding: utf-8

""" ctl for everything that can't be done without python """

from sys import argv
from dictator import Dictator
from logging import log, FATAL

def create():
    Dictator()[argv[2]] = argv[3:]


def error():
    raise ValueError(argv)


def main():
    commands = {
        'create': create,
    }
    
    assert argv[1] in commands, "Unknown command {0}".format(argv[1])
    commands.get(argv[1])()


if __name__ == '__main__':
    main()
