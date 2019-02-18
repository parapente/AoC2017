#!/usr/bin/python3


prog = []
for i in range(16):
    prog.append(chr(ord('a') + i))
with open('16.dat') as f:
    data = f.read()
data = data.rstrip()
moves = data.split(',')
print("Starting pos: ", prog)
for move in moves:
    cmd = list(move)
    if cmd[0] == 's':
        # Spin
        num = int(''.join(cmd[1:]))
        # print(prog[0:len(prog)-num])
        # print(prog[len(prog)-num:])
        prog = prog[len(prog) - num:] + prog[0:len(prog) - num]
    if cmd[0] == 'x':
        # eXchange
        pos = ''.join(cmd[1:]).split('/')
        pos = [int(pos[0]), int(pos[1])]
        prog[pos[0]], prog[pos[1]] = prog[pos[1]], prog[pos[0]]
    if cmd[0] == 'p':
        # Partner
        pos = [prog.index(cmd[1]), prog.index(cmd[3])]
        prog[pos[0]], prog[pos[1]] = prog[pos[1]], prog[pos[0]]
    # print(move, " - ", prog)
    # input()
print("Program order after dance: ", ''.join(prog))
