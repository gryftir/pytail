#!/usr/bin/env python
"""
docstring pytail
an implemtation of tail in python
"""
import sys
import os
import argparse
from collections import deque


def get_count(string):
    if string[0] == '+':
        return int( int(string[1:], 10) * -1)
    else:
        return int(string, 10)


def is_verbose(args):
    verbose = False
    if len(args.files) > 1 or args.verbose:
        verbose = True
    if args.quiet:
        verbose = False
    return verbose


def is_bytes(args):
    return args.bytes is not None


def is_lines(args):
    return args.lines is not None


def byte_or_lines(args):
    by_line = True
    string = '10'
    seek_from = os.SEEK_END
    if is_bytes(args):
        by_line = False
        string = args.bytes[0]
    elif is_lines(args):
        string = args.lines[0]
    count = get_count(string)
    if string[0] == '+':
        seek_from = os.SEEK_SET
    if count < 0:
        count += 1
    return (count, by_line, seek_from)


def by_line_print(fh, count, seek_from):
    if seek_from == os.SEEK_SET:
        #we need to skip count lines and it's negative so count up)
        for line in fh:
            if count < 0:
                count += 1
                continue
            sys.stdout.write(line)
    else:
        #need to find lines at end, this is probably inefficent
        d = deque(fh, count)
        for line in d:
            sys.stdout.write(line)


def by_byte_print(fh, count, seek_from):
    if fh is sys.stdin:
        if seek_from == os.SEEK_SET:
            fh.read(abs(count))
        else:
            data = fh.read()
            sys.stdout.write(data[ -1 * (count):])

    else:
        fh.seek(count * -1, seek_from)
    for line in fh:
        sys.stdout.write(line)


def style_print(fh, count, seek_from, by_line):
    if by_line:
        by_line_print(fh, count, seek_from)
    else:
        by_byte_print(fh, count, seek_from)


def generate_print_func(args):
    verbose = is_verbose(args)
    (count, by_line, seek_from) = byte_or_lines(args)

    def print_func(filename):
        fh = None
        print_name = filename
        if filename == '-':
            fh = sys.stdin
            print_name = 'standard input'
        else:
            try:
                fh = open(filename)
            except IOError:
                print 'pytail: can\'t open \'{}\' for reading: No such file or directory'.format(
                    filename)
                return
        if verbose:
            print '==> {} <=='.format(print_name)
        style_print(fh, count, seek_from, by_line)
        if filename != '-':
            fh.close()
        return

    return print_func


def handle_args(args):
    print_func = generate_print_func(args)
    for filename in args.files:
        print_func(filename)
    if len(args.files) == 0:
        print_func('-')


def main():
    parse = argparse.ArgumentParser(description='a python version of tail')
    #parse.add_argument('-f', '--follow',
    #description='output appended data as the file grows',
    #nargs='*')
    loud = parse.add_mutually_exclusive_group()
    loud.add_argument('-q', '--quiet', '--silent', action='store_true')
    loud.add_argument('-v', '--verbose', action='store_true')
    size = parse.add_mutually_exclusive_group()
    size.add_argument(
        '-c', '--bytes',
        nargs=1,
        help='''output the last K bytes; alternatively use -c +K
        to output bytes starting with the Kth byte of each file''')
    size.add_argument(
        '-n', '--lines',
        nargs=1,
        help='''output the last K lines, instead of the last 10;
        or use -n +k to output lines starting with the Kth''')
    parse.add_argument('files',
                       nargs='*',
                       help='''file names, defaults to stdin''')

    args = parse.parse_args()
    handle_args(args)


if __name__ == "__main__":
    main()
    pass
