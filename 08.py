import numpy as np
from scipy.linalg import eigh
from scipy.spatial.distance import pdist
from sklearn.cluster import KMeans

pos = []
for l in open('input').read().splitlines():
    pos.append(list(map(int, l.split(','))))
pos = np.array(pos)
dist = pdist(pos, metric='euclidean')
n_boxes = pos.shape[0]

# part 1
n_connections = 1000
argwhere = np.argsort(dist)[:n_connections]
iidx, jidx = np.triu_indices(len(pos), k=1)

connections = np.vstack((iidx[argwhere], jidx[argwhere])).T
adjacency = np.zeros([len(pos)]*2)
for i,j in connections:
    adjacency[i,j] = 1
    adjacency[j,i] = 1

laplacian = np.diag(np.sum(adjacency, axis=1)) - adjacency

val, vec = np.linalg.eigh(laplacian)
n_clusters = int(np.sum(val < 1e-9))

X = vec[:, :n_clusters]
cluster_ids = KMeans(n_clusters=n_clusters).fit_predict(X)
_, counts = np.unique(cluster_ids, return_counts=True)
s1 = np.prod(np.sort(counts)[-3:])

# part 2
def is_connected_graph(n_connections):
    argwhere = np.argsort(dist)[:n_connections]
    iidx, jidx = np.triu_indices(len(pos), k=1)
    connections = np.vstack((iidx[argwhere], jidx[argwhere])).T
    adjacency = np.zeros([len(pos)]*2)
    for i,j in connections:
        adjacency[i,j] = 1
        adjacency[j,i] = 1
    laplacian = np.diag(np.sum(adjacency,axis=1)) - adjacency
    val = eigh(laplacian, eigvals_only=True, subset_by_index=(0,1))
    return bool(val[1] > 1e-9)

# slight variation of pure binary search as we are looking for the smallest connection count which would connect the boxes
l = 1001
r = n_boxes*(n_boxes - 1)//2
while l <= r:
    m = l + (r - l)//2
    if is_connected_graph(m): # could be answer, set search ceiling
        n_connections = m
        r = m - 1
    else: # not enough connections, set search floor
        l = m + 1
argwhere = np.argsort(dist)[:n_connections]
iidx, jidx = np.triu_indices(len(pos), k=1)
connections = np.vstack((iidx[argwhere], jidx[argwhere])).T
s2 = pos[connections[-1][0]][0]*pos[connections[-1][1]][0]

print(s1, s2)
