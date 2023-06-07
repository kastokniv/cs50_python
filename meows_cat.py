import argparse

## use like this in terminal "meows_cat.py -n 3"
parser = argparse.ArgumentParser(description="Meow like a cat")

## if i dont specify default=1  prints meow once.
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")
