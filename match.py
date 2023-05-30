name = input("What's your name? ")

# if name == "Harry" or name == "Hermoine" or name == "Ron":
# print("gryffindor")
# elif name == "Draco":
# print("Slytherin")
# else:
# print("Who?")

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    ## _ is used to take all the other names as else
    case _:
        print("Who?")
