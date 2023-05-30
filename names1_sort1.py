names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

## to reverse add ", reverse=True"
for name in sorted(names, reverse=True):
    print(f"hello, {name}")
