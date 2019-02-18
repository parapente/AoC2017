#!/usr/bin/python3


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def snd_op(args):
    global sound
    global reg
    global pc
    pc += 1
    if is_digit(args[0]):
        sound = int(args[0])
    else:
        sound = reg[args[0]]


def set_op(args):
    global reg
    global pc
    pc += 1
    if is_digit(args[1]):
        reg[args[0]] = int(args[1])
    else:
        if args[1] in reg:
            reg[args[0]] = reg[args[1]]
        else:
            reg[args[1]] = 0
            reg[args[0]] = reg[args[1]]


def add_op(args):
    global reg
    global pc
    pc += 1
    result = 0
    if args[0] not in reg:
        reg[args[0]] = 0
    if is_digit(args[1]):
        result = reg[args[0]] + int(args[1])
    else:
        if args[1] in reg:
            result = reg[args[0]] + reg[args[1]]
        else:
            reg[args[1]] = 0
            result = reg[args[0]]
    reg[args[0]] = result


def mul_op(args):
    global reg
    global pc
    pc += 1
    result = 0
    if args[0] not in reg:
        reg[args[0]] = 0
    if is_digit(args[1]):
        result = reg[args[0]] * int(args[1])
    else:
        if args[1] in reg:
            result = reg[args[0]] * reg[args[1]]
        else:
            reg[args[1]] = 0
            result = 0
    reg[args[0]] = result


def mod_op(args):
    global reg
    global pc
    pc += 1
    result = 0
    if args[0] not in reg:
        reg[args[0]] = 0
    if is_digit(args[1]):
        result = reg[args[0]] % int(args[1])
    else:
        if args[1] in reg:
            result = reg[args[0]] % reg[args[1]]
        else:
            print("Division by zero! Exiting...")
            exit(1)
    reg[args[0]] = result


def rcv_op(args):
    global sound
    global pc
    pc += 1
    result = 0
    if is_digit(args[0]):
        result = int(args[0])
    else:
        if args[0] in reg:
            result = reg[args[0]]
        else:
            reg[args[0]] = 0
            result = 0
    if result > 0:
        print("Rcv: ", sound)
        exit(0)


def jgz_op(args):
    global reg
    global pc
    result = 0
    if is_digit(args[0]):
        result = int(args[0])
    else:
        if args[0] in reg:
            result = reg[args[0]]
        else:
            reg[args[0]] = 0
            result = 0
    if result > 0:
        off = 0
        if is_digit(args[1]):
            off = int(args[1])
        else:
            if args[1] in reg:
                off = reg[args[1]]
            else:
                reg[args[1]] = 0
                off = 0
                print("Invalid jump of zero! Exiting...")
                exit(1)
        pc = pc + off
    else:
        pc += 1


with open('18.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
prog = []
for line in lines:
    prog.append(line.split(' '))
print(prog)
prog_len = len(prog)
pc = 0
sound = -1
ops = {'snd': snd_op, 'set': set_op, 'add': add_op, 'mul': mul_op,
       'mod': mod_op, 'rcv': rcv_op, 'jgz': jgz_op}
reg = dict()
while pc >= 0 and pc < prog_len:
    print('pc:', pc, ' - ', prog[pc])
    ops[prog[pc][0]](prog[pc][1:])
