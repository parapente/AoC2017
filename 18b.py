#!/usr/bin/python3


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


def snd_op(args):
    global send
    global reg
    global pc
    global pid
    global state
    global counter
    if pid == 1:
        counter += 1
    pc[pid] += 1
    spid = (pid + 1) % 2
    if is_digit(args[0]):
        send[pid].append(int(args[0]))
    else:
        send[pid].append(reg[pid][args[0]])
    state[pid] = 2
    if state[spid] != 99:
        state[spid] = 0
        pid = spid


def set_op(args):
    global reg
    global pc
    global pid
    pc[pid] += 1
    if is_digit(args[1]):
        reg[pid][args[0]] = int(args[1])
    else:
        if args[1] in reg[pid]:
            reg[pid][args[0]] = reg[pid][args[1]]
        else:
            reg[pid][args[1]] = 0
            reg[pid][args[0]] = reg[pid][args[1]]


def add_op(args):
    global reg
    global pc
    global pid
    pc[pid] += 1
    result = 0
    if args[0] not in reg[pid]:
        reg[pid][args[0]] = 0
    if is_digit(args[1]):
        result = reg[pid][args[0]] + int(args[1])
    else:
        if args[1] in reg[pid]:
            result = reg[pid][args[0]] + reg[pid][args[1]]
        else:
            reg[pid][args[1]] = 0
            result = reg[pid][args[0]]
    reg[pid][args[0]] = result


def mul_op(args):
    global reg
    global pc
    global pid
    pc[pid] += 1
    result = 0
    if args[0] not in reg[pid]:
        reg[pid][args[0]] = 0
    if is_digit(args[1]):
        result = reg[pid][args[0]] * int(args[1])
    else:
        if args[1] in reg[pid]:
            result = reg[pid][args[0]] * reg[pid][args[1]]
        else:
            reg[pid][args[1]] = 0
            result = 0
    reg[pid][args[0]] = result


def mod_op(args):
    global reg
    global pc
    global pid
    pc[pid] += 1
    result = 0
    if args[0] not in reg[pid]:
        reg[pid][args[0]] = 0
    if is_digit(args[1]):
        result = reg[pid][args[0]] % int(args[1])
    else:
        if args[1] in reg[pid]:
            result = reg[pid][args[0]] % reg[pid][args[1]]
        else:
            print("Division by zero! Exiting...")
            exit(1)
    reg[pid][args[0]] = result


def rcv_op(args):
    global send
    global pc
    global pid
    global state
    global deadlock
    spid = (pid + 1) % 2
    if send[spid]:
        reg[pid][args[0]] = send[spid].pop(0)
        pc[pid] += 1
    else:
        # Put this pid on hold
        state[pid] = 1
        if (state[pid] == 1 and state[spid] == 1) or (state[pid] == 99 and state[spid] == 1) or (state[pid] == 1 and state[spid] == 99):
            # Deadlock
            deadlock = True
            return
        if state[spid] != 99:
            state[spid] = 0
            pid = spid


def jgz_op(args):
    global reg
    global pc
    global pid
    result = 0
    if is_digit(args[0]):
        result = int(args[0])
    else:
        if args[0] in reg[pid]:
            result = reg[pid][args[0]]
        else:
            reg[pid][args[0]] = 0
            result = 0
    if result > 0:
        off = 0
        if is_digit(args[1]):
            off = int(args[1])
        else:
            if args[1] in reg[pid]:
                off = reg[pid][args[1]]
            else:
                reg[pid][args[1]] = 0
                off = 0
                print("Invalid jump of zero! Exiting...")
                exit(1)
        pc[pid] = pc[pid] + off
    else:
        pc[pid] += 1


with open('18.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
prog = []
for line in lines:
    prog.append(line.split(' '))
# print(prog)
prog_len = len(prog)
pc = [0, 0]
pid = 0
send = [[], []]
receive = [[], []]
state = [0, -1]
# -1 waiting, 0 - Running, 1 receiving, 2 sending, 99 terminated
ops = {'snd': snd_op, 'set': set_op, 'add': add_op, 'mul': mul_op,
       'mod': mod_op, 'rcv': rcv_op, 'jgz': jgz_op}
reg = [dict(), dict()]
reg[0]['p'] = 0
reg[1]['p'] = 1
deadlock = False
counter = 0
# while pc >= 0 and pc < prog_len and not deadlock:
while not deadlock and state != [99, 99]:
    if pc[pid] < 0 or pc[pid] >= prog_len:
        state[pid] = 99
        print('Program with pid', pid, 'is teminated')
        pid = (pid + 1) % 2
    else:
        print('pc[', pid, ']:', pc[pid], ' - ', prog[pc[pid]], 'state:', state, 'snd:', [len(send[0]), len(send[1])], reg[pid])
        # input()
        # print('snd:', send)
        # print('rcv:', receive)
        ops[prog[pc[pid]][0]](prog[pc[pid]][1:])
print(state)
print(counter)
