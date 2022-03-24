import Point


class Poligon:
    def __init__(self, id):
        self.id = id
        self.points = []
        self.numberOfVertices = 0

    def AddPoint(self, newPoint):
        self.points.append(newPoint)
        self.numberOfVertices += 1

    def printPoints(self):
        print("Poligono: ", self.id)
        for point in self.points:
            point.printPoint()
        print()
