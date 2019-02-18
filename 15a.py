#!/usr/bin/python3


with open('15.dat') as f:
    gen = f.read()
gen = gen.rstrip()
gen = gen.split(',')
gen0 = int(gen[0])
gen1 = int(gen[1])
print(gen)
factor = [16807, 48271]
factor0 = 16807
factor1 = 48271
match = 0
perc = 0
for i in range(40000000000):
    gen0 = (gen0 * factor0) % 2147483647
    gen1 = (gen1 * factor1) % 2147483647
    if (gen0 & 65535) == (gen1 & 65535):
        match += 1
    newperc = (i / 40000000000) * 100
    print(newperc, "%", end='\r')
    # if newperc > perc:
    #     print(newperc, "%")
    #     perc = newperc
print(match)
