#!/usr/bin/python3


with open('17.dat') as f:
    data = f.read()
data = data.rstrip()
steps = int(data)
buf = [0]
buf_len = 1
pos = 0
perc = 0
x = 0
for i in range(50000000):
    if i == 0:
        pass
    else:
        newpos = (steps + pos) % buf_len
        # Not really needed. We just need the value
        # that is inserted in the [1] pos
        # buf.insert(newpos + 1, i)
        if newpos == 0:
            x = i
        buf_len += 1
        pos = newpos + 1
        newperc = i / 50000000 * 100
        if newperc - perc > 0.01:
            perc = newperc
            print('{:.2f}%'.format(newperc), end='\r')

print("\nNeeded value: ", x)
