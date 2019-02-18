#!/usr/bin/python3

cycles = 0
with open('6.dat') as f:
    data = f.read()
    buffers = data.split("\t")
    states = []
    for i, item in enumerate(buffers):
        buffers[i] = int(item)
    print(buffers)
    while buffers not in states:
        cycles += 1
        states.append(buffers[:])
        maxb = max(buffers)
        imax = buffers.index(maxb)
        print("max: ", maxb, " - index: ", imax)
        buffers[imax] = 0
        i = imax
        while maxb > 0:
            i += 1
            if i == 16:
                i = 0
            buffers[i] += 1
            maxb -= 1
        print(buffers)
    print("Cycles: ", cycles)
