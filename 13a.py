#!/usr/bin/python3


with open('13.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
ldict = dict()
severity = 0
for line in lines:
    tmp = line.split(": ")
    ldict[tmp[0]] = tmp[1]
for layer in ldict:
    picosec = int(layer)
    if picosec != 0:  # Alwayes crashes
        loop = (int(ldict[layer]) - 1) * 2
        if (picosec % loop) == 0:
            severity += int(layer) * int(ldict[layer])
print(severity)
