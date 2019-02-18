#!/usr/bin/python3


with open('17.dat') as f:
    data = f.read()
data = data.rstrip()
steps = int(data)
buf = [0]
pos = 0
perc = 0
for i in range(50000000):
    if i == 0:
        pass
    else:
        newpos = (steps + pos) % len(buf)
        buf.insert(newpos + 1, i)
        pos = newpos + 1
        newperc = i / 50000000 * 100
        if newperc - perc > 0.01:
            perc = newperc
            print('{:.2f}%'.format(newperc), end='\r')

print("\nNeeded value: ", buf[1])
