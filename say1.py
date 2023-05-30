import sys

## import hello function from sayings.py file to print hello
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
