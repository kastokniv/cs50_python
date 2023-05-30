with open("names.txt", "r") as file:
    # lines = file.readlines()

    # for line in lines:
    ## rstrip remove the extra space between the lines created by \n and print
    # print("hello,", line.rstrip())

    for line in file:
        print("hello,", line.rstrip())
