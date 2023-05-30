def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


## the n takes the vaue of x in the main def which is inputted by the user
def square(n):
    return n * n


## use the below to not use the same function call on other imports
if __name__ == "__main__":
    main()
