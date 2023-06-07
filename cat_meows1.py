## (n: int) is a hint that this number is a integer
## run "mypy cat_meows1.py" to check the errors and issues


## after a parentheses -> None: assigns none to the value
# def meow(n: int) -> None:
# for _ in range(n):
# print("meow")


def meow(n: int) -> str:
    return "meow\n" * n


number = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
