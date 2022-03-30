from __future__ import division
from numpy import *


from ast import Break
import Point
import Poligon
import Robot
import numpy as np

# global variables
points = {}
poligons = {}
init = Point


def readFile(path):
    file = open(path, "r")
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
            for i in range(1, len(aux) - 1):
                poligon.CreateEdge(points[aux[i]], points[aux[i+1]])
            poligons[poligon.id] = poligon
            poligons[poligon.id].printEdges()

    line = file.readline()
    aux = line.split()
    start = Point.Point("Start", float(aux[0]), float(aux[1]))
    line = file.readline()
    aux = line.split()
    finish = Point.Point("Finish", float(aux[0]), float(aux[1]))
    points["Start"] = start
    points["Finish"] = finish

    init.Point = start
    start.printPoint()
    finish.printPoint()
    print("---------------")


def perp(a):
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b

# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2


def seg_intersect(p1, p2, q1, q2):
    a1 = p1.coord
    a2 = p2.coord
    b1 = q1.coord
    b2 = q2.coord
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = dot(dap, db)
    num = dot(dap, dp)
    if denom != 0:
        intersect = (num/denom)*db + b1
        # print ("\n points are {} ={} e {} ={}".format(p1.name,a1,p2.name,a2))
        # print (" the intesercpt poits is = {} \n".format(intersect))
        if intersect[0] == a2[0] and  intersect[1]== a2[1]:
            return False
        if intersect[0] == a1[0] and  intersect[1]== a1[1]:
            return False
        
        #print(f"{p1.name}-{p2.name}   {q1.name}-{q2.name}")
        if (intersect[0] >= a1[0] and intersect[0] <= a2[0]) or (intersect[0] <= a1[0] and intersect[0] >= a2[0]):
            if (intersect[1] >= a1[1] and intersect[1] <= a2[1]) or (intersect[1] <= a1[1] and intersect[1] >= a2[1]):
                if (intersect[0] >= b1[0] and intersect[0] <= b2[0]) or (intersect[0] <= b1[0] and intersect[0] >= b2[0]):
                    if (intersect[1] >= b1[1] and intersect[1] <= b2[1]) or (intersect[1] <= b1[1] and intersect[1] >= b2[1]):
                        # print(intersect)
                        return True
        #print("Nao interceptam")
        return False


def isVisible(origin: Point, destiny: Point):
    for poligon in poligons.values():
        for edge in poligon.edges:
            if edge.p1 != destiny and edge.p2 != destiny:
                intersect = seg_intersect(origin, destiny,
                                          edge.p1, edge.p2)
                if intersect:
                    return False
    return True

def verifyIfTwoVerticesAreAdjacent(origin:Point, destiny:Point):
    for edge in poligons[findPoligon(origin)].edges:
        if (origin.name == edge.p1.name and destiny.name == edge.p2.name) or (origin.name == edge.p2.name and destiny.name == edge.p1.name):
            return True
    return False

def findNodes(origin:Point, destiny:Point):
    if destiny.name == "Start":
        return False
    if origin.name == "Start":
        return isVisible(origin, destiny)
    else:
        if itsInTheSamePoligon(origin,destiny):
            return verifyIfTwoVerticesAreAdjacent(origin,destiny)
        else:
            return isVisible(origin,destiny)
    
def findPoligon(p1:Point):
    for poligon in poligons.values():
        for point in poligon.points:
            if p1.name == point.name:
                return poligon.id        

def itsInTheSamePoligon(origin: Point, destiny: Point):
    originId=findPoligon(origin)
    destinyId=findPoligon(destiny)
    if originId == destinyId:
        return True
    else:
        return False

def findChildren(vertice: str):
    visiblePoints = []
    oringin = points[vertice]    
    for point in points.values():
        if point != oringin and findNodes(oringin, point):
            visiblePoints.append(point)
            print(f"{oringin.name} ve {point.name}")
    return visiblePoints

def main():
    readFile("entrada1.txt")
    lista=findChildren("Start")
    for lst in lista:
        print(lst.name)

    
if __name__ == "__main__":
    main()
