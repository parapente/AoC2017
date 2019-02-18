#!/usr/bin/python3


def get_group(prog):
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
    return group


with open('12.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
pdict = dict()
for line in lines:
    print(line)
    tmp = line.split(" <-> ")
    pdict[tmp[0]] = tmp[1].split(", ")
groups = []
checked = []
for p in pdict:
    if p not in checked:
        gr = get_group(p)
        groups.append(gr)
        checked += list(gr)
print("Number of groups: ", len(groups))
