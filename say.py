import cowsay
import sys

## run this in the terminal "python .\say.py Dev"
if len(sys.argv) == 2:
    # cowsay.cow("Hello, " + sys.argv[1])
    cowsay.trex("Hello, " + sys.argv[1])
