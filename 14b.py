#!/usr/bin/python3


# Function to get no of set bits in binary
# representation of positive integer n */
def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def convert_hex_to_bin(string):
    num = int(string, 16)
    s = ''
    mask = 1
    for i in range(0, 128):
        c = 1
        if (num & mask) == 0:
            c = 0
        s = str(c) + s
        mask <<= 1
    return s


def knot_hash(data):
    datalist = list(range(0, 256))
    skip = 0
    cur_pos = 0
    lengths = []
    for x, item in enumerate(data):
        lengths.append(ord(item))
    lengths = lengths + [17, 31, 73, 47, 23]
    for i in range(0, 64):
        for l in lengths:
            if (cur_pos + int(l)) <= 256:
                part = datalist[cur_pos:cur_pos+int(l)]
            else:
                part = datalist[cur_pos:256] + \
                       datalist[0:(cur_pos + int(l)) % 256]
            part.reverse()
            for x in part:
                datalist[cur_pos] = x
                cur_pos += 1
                if cur_pos == 256:
                    cur_pos = 0
            cur_pos = (cur_pos + skip) % 256
            skip += 1
    datahash = ''
    for i in range(0, 16):
        cur_pos = i * 16
        val = 0
        for j in range(0, 16):
            val ^= datalist[cur_pos+j]
        datahash += format(val, '02x')
    return datahash


def find_start(buf):
    for y in range(128):
        for x in range(128):
            if buf[y][x] == '#':
                return [y, x]
    return -1


def find_neighbours(buf, pos):
    n = []
    # Left
    if pos[1] > 0:
        if buf[pos[0]][pos[1]-1] == '#':
            n.append([pos[0], pos[1]-1])
    # Right
    if pos[1] < 127:
        if buf[pos[0]][pos[1]+1] == '#':
            n.append([pos[0], pos[1]+1])
    # Up
    if pos[0] > 0:
        if buf[pos[0]-1][pos[1]] == '#':
            n.append([pos[0]-1, pos[1]])
    # Down
    if pos[0] < 127:
        if buf[pos[0]+1][pos[1]] == '#':
            n.append([pos[0]+1, pos[1]])
    print(n)
    return n


def find_regions(regmap):
    t = regmap[:]
    for i in range(128):
        s = list(t[i])
        t[i] = s

    done = False
    region = 1
    while not done:
        pos = find_start(t)
        if pos == -1:
            done = True
        change = True
        if done:
            change = False
        neighbours = [pos]
        while change:
            p = neighbours.pop()
            t[p[0]][p[1]] = region
            n = find_neighbours(t, p)
            neighbours += n
            print("region:", region, "neigh:", neighbours)
            if not n and not neighbours:
                change = False
        if not done:
            region += 1
    return t, region-1


with open('14.dat') as f:
    key = f.read()
key = key.rstrip()
used = 0
hmap = []
for z in range(0, 128):
    row = key + '-' + str(z)
    khash = knot_hash(row)
    chash = countSetBits(int(khash, 16))
    used += chash
    # print("row: ", row, " , Knot hash: ", khash, ', used: ', chash)
    tmp = convert_hex_to_bin(khash)
    tmp = tmp.replace('1', '#')
    tmp = tmp.replace('0', '.')
    hmap.append(tmp)
tmpmap, regnum = find_regions(hmap)
for i in tmpmap:
    for j in i:
        print(j, end='')
    print('')
print("Regions: ", regnum)
