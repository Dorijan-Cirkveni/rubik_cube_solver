def Edgecycle(side):
    c = min(side, 5 - side) << 2
    X = [i + c for i in range(4)]
    return X if side < 3 else X[::-1]

def transform_edges(L, steps):
    n = len(L)
    D = dict()
    for i in range(n):
        E = L[i]
        F = L[(i - steps) % n]
        D[E] = (F, steps&1)
    return D


def transform_corners(L, steps):
    n = len(L)
    D = dict()
    for i in range(n):
        E = L[i]
        F = L[(i - steps) % n]
        D[E[0]] = (F[0], (F[1] - E[1]) % 3)
    return D


def generate_data():
    cycles = [[2, 1], [0, 2], [1, 0]]
    cycles = [e + [5 - f for f in e] for e in cycles]
    cycles += [e[::-1] for e in cycles[::-1]]
    triangles = list()
    triangle_choice = dict()
    for i in range(6):
        cycle = cycles[i]
        for j in range(4):
            tri = (i, cycle[j], cycle[(j + 1) & 3])
            ix = int(tri[1] < tri[0])
            if tri[2] < tri[ix]:
                ix = 2
            if ix == 0:
                triangle_choice[tri] = (len(triangles), 0)
                triangles.append(tri)
            else:
                tri2 = (tri + tri)[ix:][:3]
                triangle_choice[tri] = (triangle_choice[tri2][0], ix)
    return cycles, triangles, triangle_choice


def determine_edge(a: int, b: int):
    c = min({0, 1, 2} - {min(a, 5 - a), min(b, 5 - b)})
    cycle = CYCLES[c]
    ia, ib = cycle.index(a), cycle.index(b)
    if ia - ib > 1:
        ib += 4
    elif ib - ia > 1:
        ia += 4
    ret = (c << 2) + min(ia, ib)
    return ret,ia>ib


def rotation(side: int, turns: int):
    cycle = CYCLES[side]
    triangle_cycle = list()
    edge_cycle = Edgecycle(side)
    for i in range(4):
        tri = (side, cycle[i], cycle[(i + 1) & 3])
        ch = CORNER_CHOICE[tri]
        triangle_cycle.append(ch)
    triangle_transform = transform_corners(triangle_cycle,turns)
    edge_transform = transform_edges(edge_cycle,turns)
    return edge_transform, triangle_transform


CYCLES, CORNERS, CORNER_CHOICE = generate_data()


def main():
    for i in range(6):
        print(rotation(i, 1))
    return


if __name__ == "__main__":
    main()
    print("Done!")
