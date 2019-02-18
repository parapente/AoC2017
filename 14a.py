#!/usr/bin/python3


# Function to get no of set bits in binary
# representation of positive integer n */
def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


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


with open('14.dat') as f:
    key = f.read()
key = key.rstrip()
used = 0
for z in range(0, 128):
    row = key + '-' + str(z)
    khash = knot_hash(row)
    chash = countSetBits(int(khash, 16))
    used += chash
    print("row: ", row, " , Knot hash: ", khash, ', used: ', chash)
print("Used: ", used)
