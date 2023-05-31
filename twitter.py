import re

url = input("URL: ").strip()

# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

if matches := re.search(r"^https?://(www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(2))
