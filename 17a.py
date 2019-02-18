#!/usr/bin/python3


with open('17.dat') as f:
    data = f.read()
data = data.rstrip()
steps = int(data)
buf = [0]
pos = 0
for i in range(2018):
    if i == 0:
        pass
    else:
        newpos = (steps + pos) % len(buf)
        buf.insert(newpos + 1, i)
        pos = newpos + 1
print("Needed value: ", buf[pos + 1])
