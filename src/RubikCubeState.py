from src.GameState import GameState
from src.RubikCube import rotation
from src.util import decompress, compress


class RubikCubeState(GameState):
    def __init__(self, edgeData: int, cornerData: int):
        self.edgeData = edgeData
        self.cornerData = cornerData
        return

    def isFinal(self):
        raise NotImplementedError

    def nextSteps(self):
        return

    def getdata(self):
        X = [(0, 0) for i in range(12)]
        edges_raw = decompress(self.edgeData, 5)
        corners_raw = decompress(self.cornerData, 5)
        edges = ([divmod(e, 2) for e in edges_raw]+X)[:12]
        corners = (X + [divmod(e, 4) for e in corners_raw])[:8]
        return edges, corners

    def setdata(self, edges, corners):
        edges_raw = [e[0]*2+e[1] for e in edges]
        corners_raw = [e[0]*4+e[1] for e in corners]
        self.edgeData = compress(edges_raw,5)
        self.cornerData = compress(corners_raw,5)
        return

    def apply_rotation(self, side, turns):
        edges, corners = self.getdata()
        edgeRotation, cornerRotation = rotation(side, turns)
        return


if __name__ == "__main__":
    X = RubikCubeState(60, 60)
    X.apply_rotation(1, 1)
