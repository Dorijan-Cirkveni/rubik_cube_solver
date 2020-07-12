from functools import total_ordering

from src.GameState import GameState
from src.Transformation import Transformation
from src.util import *

EDGECYCLES = [
    [0, 6, 1, 4], [0, 2, 10, 3], [2, 4, 8, 5], [3, 7, 9, 6], [1, 9, 11, 8], [5, 11, 7, 10]
]
CORNERCYCLES = [
    [0, 1, 3, 2], [0, 4, 5, 1], [0, 2, 6, 4], [5, 7, 6, 4], [6, 7, 3, 2], [3, 7, 5, 1]
]


def pair(side):
    return [0, 1, 2, 2, 1, 0][side]


def get_corner(index, offset=0):
    L = list()
    for i in range(3):
        L.append(i if (index & (4 >> i)) == 0 else 5 - i)
    if index in {0, 3, 5, 6}:
        L[1], L[2] = L[2], L[1]
    offset %= 3
    if offset != 0:
        L = (L + L)[:-offset][-3:]
    return L


def get_edge(index):
    a = index // 2
    b = (pair(a) + 1) % 3
    if a % 2:
        b = 5 - b
    return a, b


def cornerside_to_location(index, offset):
    return [offset, 5 - offset][(index & (4 >> offset)) != 0]


def edgeside_to_location(index, offset):
    return get_edge(index)


def rotation(side, turns):
    turn_factor = turns & 1
    step_value = 3 - pair(side)
    turn = tuple([(step_value - i) % 3 for i in range(3)])
    etr = EDGECYCLES[side]
    ctr = CORNERCYCLES[side]
    et = generate_transformation(etr, turns, lambda x: (x, turn_factor))
    ct = generate_transformation(ctr, turns, lambda x: (x, turn))
    return Transformation(et, ct)


@total_ordering
class RubikCubeState(GameState):
    def __init__(self, edgeData: int, cornerData: int):
        self.edgeData = edgeData
        self.cornerData = cornerData
        return

    def __lt__(self, other):
        other: RubikCubeState
        if self.edgeData != other.edgeData:
            return self.edgeData < other.edgeData
        return self.cornerData < other.cornerData

    def __hash__(self):
        return hash((self.edgeData << 40) + self.cornerData)

    def isFinal(self):
        raise NotImplementedError

    def transform(self, transformation):
        transformation: Transformation
        edges, corners = self.getdata()
        newedges = []
        newcorners = []
        et = transformation.edge_transform
        ct = transformation.corner_transform
        for i in range(12):
            X = et[i] if i in et else (i, 0)
            Y = edges[X[0]]
            newedges.append((Y[0], Y[1] ^ X[1]))
        for i in range(8):
            X = ct[i] if i in ct else (i, (0, 1, 2))
            Y = corners[X[0]]
            newcorners.append((Y[0], X[1][Y[1]]))
        newstate = RubikCubeState(0, 0)
        newstate.setdata(newedges, newcorners)
        return newstate

    def nextSteps(self):
        steps = dict()
        for i in range(6):
            for j in range(1, 4):
                pass
        return steps

    def getdata(self):
        X = [(0, 0)] * 12
        edges_raw = decompress(self.edgeData, 5)
        corners_raw = decompress(self.cornerData, 5)
        edges = ([divmod(e, 2) for e in edges_raw] + X)[:12]
        corners = ([divmod(e, 4) for e in corners_raw] + X)[:8]
        return edges, corners

    def setdata(self, edges, corners):
        edges_raw = [e[0] * 2 + e[1] for e in edges][:12]
        corners_raw = [e[0] * 4 + e[1] for e in corners][:8]
        self.edgeData = compress(edges_raw, 5)
        self.cornerData = compress(corners_raw, 5)
        return

    def simpledisplay(self):
        T = [[[-1 for k in range(3)] for j in range(3)] for i in range(6)]
        edges, corners = self.getdata()
        for i in range(6):
            T[i][1][1] = i
        for i in range(12):
            e = edges[i]
            A1, A2 = get_edge(i)
            B1, B2 = get_edge(e[0])
            if e[1]:
                B1, B2 = B2, B1
        return


def main():
    for i in range(8):
        for j in range(3):
            print(get_corner(i, j), end="-")
        print()
    RC = RubikCubeState(0, 0)
    RC.setdata(identitylist(12), identitylist(8))
    X = rotation(2, 1)
    Y = RC.transform(X)
    Y.simpledisplay()
    Z=Y.getdata()
    return


if __name__ == "__main__":
    main()
