#!/usr/bin/python3


def move():
    global pos
    global direction
    global letters
    pos[0] += direction[0]
    pos[1] += direction[1]
    nextchar = lines[pos[0]][pos[1]]
    if nextchar.isalpha():
        letters.append(lines[pos[0]][pos[1]])
    else:
        if nextchar == '+':
            # We need to change direction
            if direction[0] != 0:
                # We were moving vertically, so
                # we change to moving horizontally
                testchar = lines[pos[0]][pos[1] + 1]
                if testchar.isalpha() or testchar == '-':
                    direction = [0, 1]
                else:
                    direction = [0, -1]
            else:
                # We were moving horizontally, so
                # we change to moving vertically
                testchar = lines[pos[0] + 1][pos[1]]
                if testchar.isalpha() or testchar == '|':
                    direction = [1, 0]
                else:
                    direction = [-1, 0]
        else:
            if nextchar == ' ':
                # We reached the end
                return False
    return True


with open('19.dat') as f:
    data = f.read()
lines = data.split('\n')
lines.pop()
for i in range(len(lines)):
    lines[i] = list(lines[i])
# Find start
x = 0
pos = [0, 0]
for item in lines[0]:
    if item == '|':
        pos = [0, x]
    x += 1

direction = [1, 0]
letters = []
count = 1
while move():
    count += 1
print(pos, ''.join(letters), count, 'steps')
