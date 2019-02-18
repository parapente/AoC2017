#!/usr/bin/python3

valid = 0
with open('5.dat') as f:
    data = f.read()
    jumps = data.split("\n")
    jumps.pop()
    for i, item in enumerate(jumps):
        jumps[i] = int(item)
    # print(jumps)
    lenj = len(jumps)
    pos = 0
    steps = 0
    while pos < lenj:
        jumps[pos] += 1
        pos = pos + jumps[pos] - 1
        steps += 1

print("Steps: ", steps)
