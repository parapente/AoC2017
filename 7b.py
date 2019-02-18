#!/usr/bin/python3


class prog():

    def __init__(self, initdata):
        tmp = initdata.split(" -> ")
        if len(tmp) > 1:
            self.subs = tmp[1].split(", ")
        else:
            self.subs = []
        tmp2 = tmp[0].split(" ")
        self.name = tmp2[0]
        self.weight = int(tmp2[1].strip("()"))

    def printprog(self):
        print(self.name, " - weight: ", self.weight, " - subs: ", self.subs)


def get_weight(obj):
    weight = 0
    if obj.subs:
        for s in obj.subs:
            weight += get_weight(pdict[s])
    weight += obj.weight
    return weight


def check_balance(obj):
    weights = []
    print("Checking balance of:")
    obj.printprog()
    if obj.subs:
        for s in obj.subs:
            weights.append(get_weight(pdict[s]))
        print(weights)
        values = set(weights)
        for v in values:
            if weights.count(v) == 1:
                print("Inbalance in ", obj.subs[weights.index(v)])
                check_balance(pdict[obj.subs[weights.index(v)]])
    else:
        print("Program ", obj.name, " doesn't have any subprograms.")


pdict = dict()
cycles = 0
with open('7.dat') as f:
    data = f.read()
    lines = data.split("\n")
    lines.pop()
    progs = [prog(line) for line in lines]
    for p in progs:
        pdict[p.name] = p
    root = None
    for p in progs:
        tmproot = p
        for t in progs:
            if p.name in t.subs:
                tmproot = None
        if tmproot is not None:
            root = tmproot
    print("root:")
    root.printprog()
    print("Checking weights...")
    check_balance(root)
