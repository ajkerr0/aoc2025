import numpy as np
from scipy.spatial.distance import pdist, squareform

pos = []
for i, line in enumerate(open('input').read().splitlines()):
    for j, char in enumerate(line):
        if char == '@':
            pos.append((i, j))
pos = np.array(pos)

# part 1
s1 = np.sum(np.sum(squareform(pdist(pos, metric='chebyshev')).astype(int) == 1, axis=1) < 4)

# part 2
spos = np.copy(pos)
cnt = len(spos)
while True:
    square_dists = squareform(pdist(spos, metric='chebyshev')).astype(int)
    spos = spos[np.sum(square_dists == 1, axis=1) >= 4]
    if len(spos) == cnt:
        break
    else:
        cnt = len(spos)
s2 = len(pos) - cnt
