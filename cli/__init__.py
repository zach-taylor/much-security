# python future imports
from __future__ import print_function

# system imports
import sys
import os


class CLI(object):
    HEADER = '\033[1m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @staticmethod
    def newline(num=1):
        print('\n'*num, end='')
        sys.stdout.flush()

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def print_formatted(color, message, **kwargs):
        print('%s%s%s' % (color, message, CLI.ENDC), **kwargs)
        sys.stdout.flush()

    @staticmethod
    def header(message, end='\n\n', **kwargs):
        CLI.print_formatted(CLI.HEADER, message, end=end, **kwargs)

    @staticmethod
    def success(message, **kwargs):
        CLI.print_formatted(CLI.OKGREEN, message, **kwargs)

    @staticmethod
    def info(message, **kwargs):
        CLI.print_formatted(CLI.OKBLUE, message, **kwargs)

    @staticmethod
    def warn(message, **kwargs):
        CLI.print_formatted(CLI.WARNING, message, **kwargs)

    @staticmethod
    def fail(message, **kwargs):
        CLI.print_formatted(CLI.FAIL, message, **kwargs)