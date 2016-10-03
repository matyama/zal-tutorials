#!/usr/bin/env python3

import sys


class Main:
    @staticmethod
    def main(args):
        for arg in args:
            sys.stdout.write(arg + '\n')


if __name__ == '__main__':
    Main.main(sys.argv[1:])
