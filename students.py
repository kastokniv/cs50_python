with open("students.csv") as file:
    for line in file:
        ## here the ".split(",")" will split the 2 words in the csv file differentiated bu comma
        ## name, house proides 2 vairables for to words in the csv file
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
