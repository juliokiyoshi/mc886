import Point


class Robot:

    def __init__(self, initialPosition, points):
        self.initialPosition = initialPosition
        self.visitedPoints = []
        self.unvisitedPoints = points
        self.visiblePoints = []
        self.currentPoint: Point = initialPosition
        self.distanceTraveled = 0

    def moveToPoint(self, newPoint: Point):
        self.visitedPoints.append(self.currentPoint)
        self.distanceTraveled += newPoint.DistanceToPoint(self.currentPoint)
        self.currentPoint = newPoint
        self.visiblePoints.clear()
        self.unvisitedPoints.remove(newPoint)

    def printVisitedPoints(self):
        print("PONTOS VISITADOS: ")
        for point in self.visitedPoints:
            print(point.name + "->", end="")
        print()

    def printVisiblePoints(self):
        print("PONTOS VISIVEIS: ")
        for point in self.visiblePoints:
            print(point.name + "->", end="")
        print()

    def addVisiblePoint(self, newPoint):
        self.visiblePoints.append(newPoint)
