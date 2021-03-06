#!/usr/bin/env python3

import sys

if __name__ == '__main__':

    # Implement simple program that takes two string arguments and prints them to the stdout - earch on a new line.

    # What if there is less/more than 2 arguments?
    if len(sys.argv) != 3:
        err = 'Error: two arguments expected, given {:d}\n'.format(len(sys.argv) - 1)
        sys.stdout.write(err)
        exit(1)

    # In this exercise we use sys.stdout.write() instead of print(), notice the newline character '\n'.
    output = '{:s}\n{:s}\n'.format(sys.argv[1], sys.argv[2])
    sys.stdout.write(output)
