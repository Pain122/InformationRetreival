# Team Pavel Tishkin and Ruslan Mihailov
from annoy import AnnoyIndex
from scipy.spatial import KDTree

# Copied from the assignment notebook
def build(N, D):
    dataset = [None] * N
    for i in range(N):
        dataset[i] = [((i % 9997 - d) + (i * d - d)) % 9999 for d in range(D)]
        dataset[i] = tuple(dataset[i])
    return dataset
DATASET = build(100000, 3)

n_trees = 7
dim = 3
with open('input.txt', 'r') as file:
    method, vector = file.read().split('\n')
v = tuple(map(int, vector.split(' ')))
# Following the examples and docs from https://github.com/spotify/annoy
if method == 'annoy':
    # Initializing Annoy Index
    t = AnnoyIndex(dim, 'euclidean')
    for i in range(len(DATASET)):
        t.add_item(i, DATASET[i])
    t.build(n_trees)
    result = t.get_nns_by_vector(v, 1, include_distances=False)[0]
    with open('output.txt', 'w+') as o:
        o.write(str(result))
if method == 'kdtree':
    # Using only Scipy documentation
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html
    # https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.query.html
    t = KDTree(DATASET)
    d, result = t.query(x=v, p=2)
    with open('output.txt', 'w+') as o:
        o.write(str(result))