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
        self.weight = tmp2[1].strip("()")

    def printprog(self):
        print(self.name, " - weight: ", self.weight, " - subs: ", self.subs)


cycles = 0
with open('7.dat') as f:
    data = f.read()
    lines = data.split("\n")
    lines.pop()
    progs = [prog(line) for line in lines]
    root = None
    for p in progs:
        tmproot = p
        for t in progs:
            if p.name in t.subs:
                tmproot = None
        if tmproot is not None:
            root = tmproot
    root.printprog()
