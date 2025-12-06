inp = open('input').read().splitlines()
blank_idx = inp.index('')
ranges = inp[:blank_idx]
ids = inp[blank_idx+1:]

# part 1
s1 = 0
for id in map(int, ids):
    for range in ranges:
        start, stop = map(int, range.split('-'))
        if id >= start and id <= stop:
            s1 += 1
            break

# part 2
s2 = 0
while True:
    if len(ranges) == 0:
        break
    irange = ranges[0]
    istart, istop = map(int, irange.split('-'))
    for j, jrange in enumerate(ranges[1:]):
        jstart, jstop = map(int, jrange.split('-'))
        ostart = max(istart, jstart)
        ostop = min(istop, jstop)
        if ostart <= ostop: # jrange intersects irange
            new_range = str(min(istart, jstart)) + '-' + str(max(istop, jstop))
            ranges[0] = new_range
            del ranges[j+1]
            break
    else: # irange is disjoint
        s2 += istop - istart + 1
        del ranges[0]

print(s1, s2)
