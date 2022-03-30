import Point


class Line:
    def __init__(self, point1, point2) -> None:
        self.p1 = point1
        self.p2 = point2
        self.lenght = point1.DistanceToPoint(point2)
