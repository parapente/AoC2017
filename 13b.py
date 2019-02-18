#!/usr/bin/python3


def crashes(offset):
    for layer in ldict:
        picosec = int(layer) + offset
        loop = (int(ldict[layer]) - 1) * 2
        if (picosec % loop) == 0:
            return True
    return False


with open('13.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
ldict = dict()
for line in lines:
    tmp = line.split(": ")
    ldict[tmp[0]] = tmp[1]
off = 0
while crashes(off):
    off += 1
print("Smallest offset: ", off)
