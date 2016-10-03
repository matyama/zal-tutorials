#!/usr/bin/env python3

import sys

if __name__ == '__main__':

    if len(sys.argv) != 3:
        err = 'Error: two arguments expected, given {:d}\n'.format(len(sys.argv) - 1)
        sys.stdout.write(err)
        exit(1)

    output = '{:s}\n{:s}\n'.format(sys.argv[1], sys.argv[2])

    sys.stdout.write(output)
