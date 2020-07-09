from functools import total_ordering

from src.GameState import GameState
from src.RubikCube import rotation
from src.util import decompress, compress


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

    def nextSteps(self):
        steps = dict()
        for i in range(6):
            for j in range(1, 4):
                nextstate = self.apply_rotation(i, j)
                steps[(i, j)] = nextstate
        return steps

    def getdata(self):
        X = [(0, 0)]*12
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

    def apply_rotation(self, side, turns):
        edges, corners = self.getdata()
        edgeRotation, cornerRotation = rotation(side, turns)
        newstate = RubikCubeState(0, 0)
        newedges = []
        for i in range(12):
            if i in edgeRotation:
                er = edgeRotation[i]
                newedge = edges[er[0]]
                renewededge = (newedge[0], (newedge[1] + er[1]) % 2)
                newedges.append(renewededge)
            else:
                newedges.append(edges[i])
        newcorners = []
        for i in range(8):
            if i in cornerRotation:
                cr = cornerRotation[i]
                newcorner = corners[cr[0]]
                renewedcorner = (newcorner[0], (newcorner[1] + cr[1]) % 3)
                newcorners.append(renewedcorner)
            else:
                newcorners.append(corners[i])
        newstate.setdata(newedges, newcorners)
        return newstate


if __name__ == "__main__":
    _a = [(i, 0) for i in range(12)]
    _b = [(i, 0) for i in range(8)]
    _X = RubikCubeState(0, 0)
    _X.setdata(_a, _b)
    print(_X.getdata())
    _Y = _X.apply_rotation(0, 1)
    print(_Y.getdata())
