#!/usr/bin/python3


prog = []
for i in range(16):
    prog.append(chr(ord('a') + i))
with open('16.dat') as f:
    data = f.read()
data = data.rstrip()
moves = data.split(',')
print("Starting pos: ", prog)
perc = 0
state = dict()
for j in range(1000000000):
    key = ''.join(prog)
    if key in state:
        prog = state[key]
        # print('here! key=', key, ' prog:', state[key])
    else:
        start = prog[:]
        for move in moves:
            cmd = list(move)
            if cmd[0] == 's':
                # Spin
                num = int(''.join(cmd[1:]))
                # print(prog[0:len(prog)-1])
                # print(prog[len(prog)-1])
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
        # print("Adding key='", key, "' - ", prog)
        state[key] = prog[:]
    # print("New prog: ", prog)
    newperc = (j / 1000000000) * 100
    if (newperc - perc) > 0.01:
        perc = newperc
        print('{:.2f}%'.format(newperc), end='\r')

print("Program order after 1000000000 dances: ", ''.join(prog))
