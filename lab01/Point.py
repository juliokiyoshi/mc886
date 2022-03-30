import math
import numpy as np


class Point:
    def __init__(self, name, x: float, y: float):
        self.name = name
        self.coord = np.array([x, y])
        self.visit = False

    def printPoint(self):
        print(self.name + ":", self.coord)

    def DistanceToPoint(self, point) -> int:
        dst = math.sqrt((self.coord[0] - point.coord[0]) * (self.coord[0] - point.coord[0])
                        + (self.coord[1] - point.coord[1])*(self.coord[1] - point.coord[1]))
        return dst
