#!/usr/bin/env python3

import sys


class Main:
    """
    Main class.

    Implement one static method (use @staticmethod annotation and do not use self as parameter)
    that takes one parameter - a list of arguments and prints them, one per line, on the standard output.
    """

    @staticmethod
    def main(args):
        for arg in args:
            sys.stdout.write(arg + '\n')


if __name__ == '__main__':
    # call the Main class' main method with all program arguments except the program name
    Main.main(sys.argv[1:])
