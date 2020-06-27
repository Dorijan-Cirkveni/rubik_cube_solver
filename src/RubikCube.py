'''
Corner -> 3 bits, each bit indicate which side is used
[0|5][1|4][2|3]
Edge -> 12 edges, 4 per side pair
'''


def pairnumber(n):
    return [n, 5 - n][n > 2]


def generate_data():
    cycles = [[2, 1], [0, 2], [1, 0]]
    cycles = [e + [5 - f for f in e] for e in cycles]
    cycles += [e[::-1] for e in cycles[::-1]]
    return cycles


CYCLES = generate_data()


def indexToCorner(n):
    L = list(bin(n)[-3:])
    R = [[i, 5 - i][L[i]] for i in range(3)]
    return R


def cornerToIndex(R):
    n = 0
    for i in range(3):
        n += (int(R[i] > 2)) << i
    return


def indexToEdge(n):
    c, ind = divmod(n, 4)
    XT = CYCLES[c]
    X = XT + XT[:1]
    return XT[ind], XT[ind + 1]


def edgeToIndex(a, b):
    c = 3 - a - b
    XT = CYCLES[c]
    X = XT + XT[:1]
    ia = X.index(a)
    ib = X.index(b)
    if ia > ib + 1:
        ib += 4
    elif ib > ia + 1:
        ia += 4
    return


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
    triangle_cycle = list()
    edge_cycle = []
    triangle_transform = transform_corners(triangle_cycle, turns)
    edge_transform = transform_edges(edge_cycle, turns)
    return edge_transform, triangle_transform


def main():
    return


if __name__ == "__main__":
    main()
    print("Done!")
