#!/usr/bin/python3

valid = 0
with open('4.dat') as f:
    data = f.read()
    passphrases = data.split("\n")
    for passphrase in passphrases:
        tmp = passphrase.split(" ")
        if passphrase != "" and (len(tmp) == len(set(tmp))):
            print(passphrase, " is valid")
            valid += 1

print("Valid passphrases: ", valid)
