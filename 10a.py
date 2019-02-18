#!/usr/bin/python3


datalist = list(range(0, 256))
skip = 0
cur_pos = 0
with open('10.dat') as f:
    data = f.read()
lengths = data.split(",")
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
print("Hash check: ", datalist[0] * datalist[1])
