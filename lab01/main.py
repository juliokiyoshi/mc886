import Point
import Poligon


def main():
    file = open("lab01\entrada1.txt", "r")
    points = {}
    poligons = {}

    pos = 0
    for line in file:
        if(line[0] == "\n"):
            print("---------------")
            break
        aux = line.split()
        if(line[0].isalpha()):
            points[str(line[0])] = (Point.Point(
                aux[0], float(aux[1]), float(aux[2])))
            points[line[0]].printPoint()

    for line in file:
        if(line[0] == "\n"):
            print("---------------")
            break
        aux = line.split()
        if(len(line) > 2):
            poligon = Poligon.Poligon(int(aux[0]))
            for i in aux[1:]:
                poligon.AddPoint(points[i])
            poligons[poligon.id] = poligon
            poligons[poligon.id].printPoints()

            # points[i].printPoint()
    line = file.readline()
    aux = line.split()
    start = Point.Point("Start", float(aux[0]), float(aux[1]))
    line = file.readline()
    aux = line.split()
    finish = Point.Point("Finish", float(aux[0]), float(aux[1]))
    points["Start"] = start
    points["Finish"] = finish

    start.printPoint()
    finish.printPoint()


if __name__ == "__main__":
    main()
