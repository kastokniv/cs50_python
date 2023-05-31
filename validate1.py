import re

email = input("What's your email? ").strip()

## using regex to verify the email address is valid or invalid
## using the regex expresion of re libirary
## r indicates the raw string
## \w represents [a-zA-Z0-9_]
## re.IGNORECASE Perform case-insensitive matching
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
