#!/usr/bin/python3


with open('11.dat') as f:
    data = f.read()
data = data.strip('\n')
steps = data.split(",")
# Simplify steps
# Cancel out steps in opposite directions
opposite = {'n': 's', 'se': 'nw', 'ne': 'sw'}
for o in ['n', 'se', 'ne']:
    done = False
    while not done:
        try:
            s1 = steps.index(o)
            s2 = steps.index(opposite[o])
            del steps[s1]
            s2 = steps.index(opposite[o])
            del steps[s2]
        except ValueError:
            done = True
# Simple vector math
# nw + s = sw, ne + s = se, sw + n = nw, se + n = ne
math = {('nw', 's'): 'sw', ('ne', 's'): 'se', ('sw', 'n'): 'nw',
        ('se', 'n'): 'ne', ('se', 'sw'): 's', ('ne', 'nw'): 'n'}
directions = ['n', 's', 'ne', 'se', 'nw', 'sw']
for x in directions:
    for y in directions:
        if (x, y) in math.keys():
            done = False
            while not done:
                try:
                    s1 = steps.index(x)
                    s2 = steps.index(y)
                    steps[s1] = math[(x, y)]
                    del steps[s2]
                except ValueError:
                    done = True
print(steps)
print('You need to make ', len(steps), ' steps')
