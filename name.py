import sys

## ~type this in terminal~ "python .\name.py Dev"
## use try as an exception so that "python name.py" don't show error
## sys.argv[1] gives the user input name as 1 beacause the file name is 0
## here len is the length of the input string

# try:
# print("Hello, My name is", sys.argv[1])
# except IndexError:
# print("Too few arguments")

# here we check if input is 2 argument or more
# if len(sys.argv) < 2:
# print("Too few arguments")
# elif len(sys.argv) > 2:
# print("Too many arguments")
# else:
# print("Hello, My name is", sys.argv[1])

## to exit sys after the code line is unfullfilled
# if len(sys.argv) < 2:
# sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
# sys.exit("Too many arguments")

## print the name tags
# print("Hello, My name is", sys.argv[1])

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

## to start the argument at 1 and end use sys.argv[1:]:
for arg in sys.argv[1:]:
    print("Hello, My name is", arg)
