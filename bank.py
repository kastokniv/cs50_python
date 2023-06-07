balance = 0


## you can read the value of a global variable out of a method definition
## you cannot write/append/write the vlaue of a global variable out of a method
def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    ## global keyword allows to use a global variable and write/append/write the vlaue
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()
