import re

name = input("What's your name? ").strip()

## := walrus operator ## Do something with match with if statement
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")
