## Ask user for their name also Remove whitespace from str & capitalize
name = input("What's your name? ").strip().title()

## Split user name into first and last
first, last = name.split(" ")

## Say Hello to user
print(f"Hello, {name}")
