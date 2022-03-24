import Point


class Poligon:
    def __init__(self, id):
        self.id = id
        self.points = []

    def AddPoint(self, newPoint):
        self.points.append(newPoint)

    def printPoints(self):
        print("Poligon: ", self.id)
        for point in self.points:
            point.printPoint()
        print()
