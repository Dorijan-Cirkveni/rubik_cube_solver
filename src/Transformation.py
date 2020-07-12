from src.util import combine_transformations


def combineEdgeTuples(a, b):
    return a[0], a[1] ^ b[1]


def combineCornerTuples(a, b):
    T = tuple([a[1][b[1][i]] for i in range(3)])
    return a[0], T


class Transformation:
    def __init__(self, edge_transform, corner_transform):
        self.edge_transform = edge_transform
        self.corner_transform = corner_transform
        return

    def __add__(self, other):
        other: Transformation
        newedge = combine_transformations(self.edge_transform,
                                          other.edge_transform,
                                          combineEdgeTuples)
        newcorner = combine_transformations(self.corner_transform,
                                            other.corner_transform,
                                            combineCornerTuples)
        return Transformation(newedge,newcorner)
