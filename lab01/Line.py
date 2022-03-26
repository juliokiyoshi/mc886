import Point


class Line:
    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2
        self.lenght = point1.DistanceToPoint(point2)
        yoyo = point2.coord[1]-point1.coord[1]
        xoxo = (point2.coord[0]-point1.coord[0])
        self.slope = yoyo/xoxo if xoxo != 0 else float('inf')

        self.b = point1.coord[1] - self.slope * \
            point1.coord[0] if self.slope != 0 else 0

    def PrintLine(self):
        print("Line from", self.point1.name, "to", self.point2.name,
              ": slope =", self.slope, "\tb =", self.b)

    def Intercept(origin, destiny) -> bool:
        return
