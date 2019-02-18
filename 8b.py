#!/usr/bin/python3


reg = dict()
highest = 0


def check_condition(cond):
    if cond[0] not in reg.keys():
        reg[cond[0]] = 0
    c = str(reg[cond[0]]) + cond[1] + str(cond[2])
    return eval(c)


def parse_line(line):
    global highest
    cmd = line.split(" ")
    if cmd[0] not in reg.keys():
        reg[cmd[0]] = 0
    cond = cmd[4:]
    if check_condition(cond):
        if cmd[1] == 'inc':
            reg[cmd[0]] += int(cmd[2])
            if reg[cmd[0]] > highest:
                highest = reg[cmd[0]]
        else:
            reg[cmd[0]] -= int(cmd[2])
            if reg[cmd[0]] > highest:
                highest = reg[cmd[0]]


with open('8.dat') as f:
    data = f.read()
    lines = data.split("\n")
    lines.pop()
    for l in lines:
        parse_line(l)
    maxval = 0
    for k in reg:
        if reg[k] > maxval:
            maxval = reg[k]
    print("The largest value in any register is ", maxval)
    print("The highest value held in any register during the process is ", highest)
