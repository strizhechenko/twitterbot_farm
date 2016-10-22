# coding: utf-8

""" ctl for everything that can't be done without python """

from sys import argv
from dictator import Dictator
from logging import log, FATAL

def auth():
    user, token, secret = argv[2:]
    d = Dictator()
    user_data = d[user]
    user_data[2], user_data[3] = token, secret
    d[user] = user_data


def main():
    commands = {
        'auth': auth,
    }
    
    assert argv[1] in commands, "Unknown command {0}".format(argv[1])
    commands.get(argv[1])()


if __name__ == '__main__':
    main()
