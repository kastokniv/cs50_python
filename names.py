name = input("What's your name? ")

# file = open("names.txt", "a")  ## open file with 'a' to append the new file
# file.write(f"{name}\n")  ## write names in the file
# file.close()  ## close the file

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
