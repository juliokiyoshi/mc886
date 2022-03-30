import Point
import Line


class Poligon:
    def __init__(self, id):
        self.id = id
        self.points = []
        self.numberOfVertices = 0
        self.edges = []

    def AddPoint(self, newPoint):
        self.points.append(newPoint)
        self.numberOfVertices += 1

    def CreateEdge(self, point1: Point, point2: Point):
        edge = Line.Line(point1, point2)
        self.edges.append(edge)

    def printPoints(self):
        print("Poligono: ", self.id)
        for point in self.points:
            point.printPoint()
        for edge in self.edges:
            edge.PrintLine()
        print()

    def printEdges(self):
        print("Poligono: ", self.id)
        for edge in self.edges:
            print(
                f"{edge.p1.name}{edge.p1.coord} {edge.p2.name}{edge.p2.coord}")
