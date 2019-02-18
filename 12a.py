#!/usr/bin/python3


def count_con(prog):
    visited = []
    tovisit = [prog]
    group = set()
    group.add(prog)
    done = False
    while not done:
        try:
            last = tovisit.pop()
            if last not in visited:
                visited.append(last)
                nodes = pdict[last]
                for t in nodes:
                    group.add(t)
                tovisit += nodes
        except IndexError:
            done = True
    return len(group)


with open('12.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
pdict = dict()
for line in lines:
    print(line)
    tmp = line.split(" <-> ")
    pdict[tmp[0]] = tmp[1].split(", ")
print(count_con("0"))
