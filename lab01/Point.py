class Point:
    name = ""
    coord = ()
    def __init__(self, name, x, y):
        self.name = name
        self.coord = (x, y)


    def printPoint(self):
        print(self.name + ":", self.coord)