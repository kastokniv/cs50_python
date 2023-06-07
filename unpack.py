def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


## list of coins
## use ** to unpack dictionary
# coins = [100, 50, 25]
# print(total(*coins), "knuts")


## dictionary or dict of coins
## use ** to unpack dictionary
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins), "knuts")
