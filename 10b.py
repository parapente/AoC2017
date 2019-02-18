#!/usr/bin/python3


datalist = list(range(0, 256))
skip = 0
cur_pos = 0
lengths = []
with open('10.dat') as f:
    data = f.read()
for x in range(0, len(data)-1):
    lengths.append(ord(data[x]))
lengths = lengths + [17, 31, 73, 47, 23]
for i in range(0, 64):
    for l in lengths:
        print("length: ", int(l), ", cur_pos: ", cur_pos, ", skip: ", skip)
        if (cur_pos + int(l)) <= 256:
            part = datalist[cur_pos:cur_pos+int(l)]
        else:
            part = datalist[cur_pos:256] + datalist[0:(cur_pos + int(l)) % 256]
        part.reverse()
        print(part)
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
print("Knot hash: ", datahash)
