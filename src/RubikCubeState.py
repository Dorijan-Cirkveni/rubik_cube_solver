from functools import total_ordering

from src.GameState import GameState
from src.util import *

EDGECYCLES = [
    [0, 6, 1, 4], [0, 2, 10, 3], [2, 4, 8, 5], [3, 7, 9, 6], [1, 9, 11, 8], [5, 11, 7, 10]
]
CORNERCYCLES = [
    [0, 1, 3, 2], [0, 4, 5, 1], [0, 2, 6, 4], [5, 7, 6, 4], [6, 7, 3, 2], [3, 7, 5, 1]
]


def get_corner(index):
    L = list()
    for i in range(3):
        L.append(i if (index & (4 >> i)) == 0 else 5 - i)
    if index in {0, 3, 5, 6}:
        L[1], L[2] = L[2], L[1]
    return L


def rotation(side, turns):
    etr = EDGECYCLES[side]
    ctr = CORNERCYCLES[side]
    et = transformation(etr, turns)
    ct = transformation(ctr, turns)
    turn_factor = turns & 1
    step_value = 3 - side
    etf = {e: (et[e], turn_factor) for e in et}
    ctf = dict()
    crn = {e: set(get_corner(e)) for e in ctr}
    for e in ct:
        eL = crn[e]-{side}
        eL2 = crn[ct[e]]-{side}

    return


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

    def transform(self):

        return

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


def main():
    RC = RubikCubeState(0, 0)
    X = [get_edge(i) for i in range(8)]
    RC.setdata(identitylist(12), identitylist(8))
    rotation(0, 1)
    return


if __name__ == "__main__":
    main()
