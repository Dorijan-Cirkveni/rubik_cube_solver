from src.GameState import GameState
from src.RubikCube import rotation
from src.util import decompress


class RubikCubeState(GameState):
    def __init__(self, edgeData: int, cornerData:int):
        self.edgeData = edgeData
        self.cornerData = cornerData
        return

    def isFinal(self):
        raise NotImplementedError

    def nextSteps(self):
        return

    def apply_rotation(self,side,turns):
        edgeRotation, cornerRotation = rotation(side,turns)
        edges_raw = decompress(self.edgeData,5)
        corners_raw = decompress(self.cornerData,5)
        edges=[divmod(e,4) for e in edges_raw]
        corners=[divmod(e,4) for e in corners_raw]

