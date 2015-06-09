# pytail
a somewhat posix compliant implementation of tail in python

what works

-c for bytes including -c 1 and -c +1 for starting byte
-n for lines including -n 1 and -n +1 for starting line

works from both stdin and files
verbose and quiet both work
basic help works
works for multiple files including - as stdin as per posix

TODO:
haven't implemented -f/--follow yet




