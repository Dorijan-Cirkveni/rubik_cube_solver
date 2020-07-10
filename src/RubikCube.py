'''
Corner -> 3 bits, each bit indicate which side is used
[0|5][1|4][2|3]
Edge -> 12 edges, 4 per side pair
'''


def pairnumber(n):
    return [n, 5 - n][n > 2]


CYCLES = [[2, 1, 3, 4], [0, 2, 5, 3], [1, 0, 4, 5], [5, 4, 0, 1], [3, 5, 2, 0], [4, 3, 1, 2]]


def indexToCorner(n, offset=0):
    L = [int(e) for e in bin(8+n)[-3:]]
    R = [[i, 5 - i][L[i]] for i in range(3)]
    return (R + R)[3 - offset:][:3]


def cornerToIndex(R):
    n = 0
    X = [pairnumber(e) for e in R]
    for i in range(3):
        n += (int(R[i] != X[i])) << i
    return n,X.index(0)


def indexToEdge(n):
    c, ind = divmod(n, 4)
    XT = CYCLES[c]
    X = XT + XT[:1]
    return XT[ind], XT[ind + 1]


def edgeToIndex(a, b):
    c = 3 - pairnumber(a) - pairnumber(b)
    XT = CYCLES[c]
    X = XT + XT[:1]
    ia = X.index(a)
    ib = X.index(b)
    if ia > ib + 1:
        ib += 4
    elif ib > ia + 1:
        ia += 4
    return (c << 2) + min(ia, ib), ia > ib


def transform_edges(L, steps):
    n = len(L)
    D = dict()
    for i in range(n):
        E = L[i]
        F = L[(i - steps) % n]
        D[E] = (F, steps & 1)
    return D


def transform_corners(L, steps):
    n = len(L)
    D = dict()
    for i in range(n):
        E = L[i]
        F = L[(i - steps) % n]
        D[E[0]] = (F[0], (F[1] - E[1]) % 3)
    return D


def rotation(side: int, turns: int):
    cycle = CYCLES[side]
    triangle_cycle = []
    edge_cycle = [edgeToIndex(side, e) for e in cycle]
    triangle_transform = transform_corners(triangle_cycle, turns)
    edge_transform = transform_edges(edge_cycle, turns)
    return edge_transform, triangle_transform


def main():
    A=[indexToCorner(i,1) for i in range(8)]
    B=[cornerToIndex(e) for e in A]
    return


if __name__ == "__main__":
    main()
    print("Done!")
