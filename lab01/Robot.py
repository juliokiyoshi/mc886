import Point


class Robot:

    def __init__(self, initialPosition, points):
        self.initialPosition = initialPosition
        self.visitedPoints = [initialPosition]
        self.points = points
        self.unvisitedPoints = list(points.values())
        self.unvisitedPoints.remove(initialPosition)
        self.visiblePoints = []
        self.currentPoint: Point = initialPosition
        self.distanceTraveled = 0

    def moveToPoint(self, newPoint: Point):
        cost = newPoint.DistanceToPoint(self.currentPoint)
        self.distanceTraveled += cost
        self.currentPoint = newPoint
        self.visiblePoints.clear()
        if newPoint != self.initialPosition:
            self.visitedPoints.append(newPoint)
        if newPoint in self.unvisitedPoints:
            self.unvisitedPoints.remove(newPoint)
        return cost

    def printVisitedPoints(self):
        print("PONTOS VISITADOS: ")
        for point in self.visitedPoints:
            if point.name == 'Finish':
                print(point.name)
            else:
                print(point.name + "->", end="")
        print(str(len(self.visitedPoints)) + " pontos visitados")

    def printVisiblePoints(self):
        print("PONTOS VISIVEIS: ")
        for point in self.visiblePoints:
            print(f"{point.name}{point.coord}", end="  ")
        print()

    def printUnvisitedPoints(self):
        print("PONTOS NAO VISITADOS: ")
        for point in self.unvisitedPoints:
            print(point.name + ", ", end="")
        print()

    def addVisiblePoint(self, newPoint):
        self.visiblePoints.append(newPoint)

    def isVisited(self, point):
        return True if point in self.visitedPoints else False

    def isCurrentPoint(self, point):
        return self.currentPoint == point

    def restart(self):
        self.visitedPoints = [self.initialPosition]
        self.unvisitedPoints = list(self.points.values())
        self.unvisitedPoints.remove(self.initialPosition)
        self.visiblePoints = []
        self.currentPoint: Point = self.initialPosition
        self.distanceTraveled = 0