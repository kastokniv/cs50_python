email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".com"):
    print("Valid")
else:
    print("Invalid")
