while True:
    try:
        x = int(input("What's x? "))

    except ValueError:
        print("x is not an integer")

    else:
        break

## f is a format string to interpolate curly brackets {x}
print(f"x is {x}")
