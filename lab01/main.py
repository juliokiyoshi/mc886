from __future__ import division


from ast import Break
import Point
import Poligon
import Robot
import numpy as np

# global variables
points = {}
poligons = {}
init = Point
array_distances = []
ordenation_distances = []
global_origin_distances_to_other_vertices = {}


# auxiliar functions
def itsPossibleToTravel(actualVertice, DestinyVertice, poligonoOrigem, poligonoDestino):
    if actualVertice == "Start":
        return True
    elif actualVertice != "Start" and poligonoOrigem == poligonoDestino:
        return True
    else:
        isVisible(actualVertice, DestinyVertice)

# função para calular se o segmento r1r2 intercepta algum poligono ainda incompleta

# retorna True se nao intersecta

# retorna true se r2 é visivel de r1
# retorna false se nao


def isVisible(r1, r2):
    for poligon in poligons.values():
        for edge in poligon.edges:
            intersectionPoint = intersection(
                line(r1, r2), line(edge.point1.coord, edge.point2.coord))
            if(intersectionPoint):
                #print(f"Intersecao de {r1} {r2} para {edge.point1.name}{edge.point1.coord} {edge.point2.name}{edge.point2.coord} em {intersectionPoint}")
                return False
    print("{} consegue ver {}".format(r1, r2), end=" ")
    return True


# Função para calcular se o segmento r1r2 e o segmento r3r4 se cruzam
# para mais informações:  https://stackoverflow.com/questions/3252194/numpy-and-line-intersections
# retorna True se ha interseccao
def findIfIntersect(r1, r2, r3, r4):
    # print(r1, r2, r3, r4)
    a1 = np.array(r1)
    a2 = np.array(r2)
    b1 = np.array(r3)
    b2 = np.array(r4)
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = np.dot(dap, db)
    num = np.dot(dap, dp)
    # print("values of da = {} db = {} and dap ={} and denom = {}".format(da, db, dap, denom))
    if denom == 0:  # se denom == 0 eles nunca se cruzam caso contrario existe um ponto de intersecção entre duas retas
        return False
    else:
        interceptionPoint = (num / denom.astype(float))*db + b1
        if(interceptionPoint[0] > a1[0] and interceptionPoint[0] < a2[0]) \
                or (interceptionPoint[0] < a1[0] and interceptionPoint[0] > a2[0]):
            print("Interception Point: ", interceptionPoint)
            return True
        else:
            return False


def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C


def intersection(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        if (x >= L1[0] and x <= L2[0]) or (x <= L1[0] and x >= L2[0]):
            if(y >= L1[1] and y <= L2[1]) or (y <= L1[1] and y >= L2[1]):
                return x, y
        else:
            return False
    else:
        return False


def perp(a):
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


def getKey(dct, value):
    return [key for key in dct if (dct[key] == value)]


# função que acha em qual poligono está um vertice
def findPoligon(vertice, poligonsList):
    for list in poligonsList:
        for pts in list.points:
            if pts.name == vertice:
                return list.id


def ordenationDistancesFromTheActualVertice(vertice, dict, sortedList):
    listOfPoints = list(points.values())
    list = []
    for point in listOfPoints:
        if point.name != "Start" and point.visit != False:
            pt1 = np.array(point.coord)
            pt2 = np.array(vertice.coord)
            dist = np.linalg.norm(pt1 - pt2)
            list.append(dist)
            dict[point.name] = dist
    temp = array_distances
    temp = np.sort(temp)
    for dist in temp:
        sortedList.append(dist)

    return dict, sortedList


def ordenationDistancesBeteweenOriginAndAllVerices(origin):
    listOfPoints = points.values()
    for point in listOfPoints:
        if point.name != "Start":
            pt1 = np.array(point.coord)
            pt2 = np.array(origin.coord)
            dist = np.linalg.norm(pt1 - pt2)
            array_distances.append(dist)
            global_origin_distances_to_other_vertices[point.name] = dist

    temp = array_distances
    temp = np.sort(temp)
    for dist in temp:
        ordenation_distances.append(dist)


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

# def moviment(vertice,pos):
#     if(pos== 10):
#         return
#     print(pos)
#     if vertice == init.Point.name:
#         ordenationDistancesBeteweenOriginAndAllVerices(init.Point)
#         NewVertice = getKey(global_origin_distances_to_other_vertices,ordenation_distances[pos])[0]
#         lst= list(poligons.values())
#         poligonId=findPoligon(NewVertice,lst)
#         control_variables=itsPossibleToTravel(init.Point.name,poligonId,"zero",poligonId)
#         if control_variables == True:
#             print("next vertice is: {} \n".format(NewVertice))
#             pos+=1
#             moviment(vertice,pos)
#     else:
#         # calculate the distances to the new vertices
#         #findNewVertices(vertice)
#         NewVertice = getKey(global_origin_distances_to_other_vertices,ordenation_distances[0])[pos]
#         lst= list(poligons.values())
#         poligonId=findPoligon(NewVertice,lst)
#         control_variables=itsPossibleToTravel(init.Point.name,poligonId,"zero",poligonId)
#         if control_variables == True:
#             print("next vertice is: {} \n".format(NewVertice))
#             i+=1
#             moviment(vertice,pos)


def main():
    readFile("entrada1.txt")
    print("partindo da origem temos a seguinte sequencia \n")
    robot = Robot.Robot(points["Start"], points)
    robot.printUnvisitedPoints()
    visiblePoints = []
    for point in robot.unvisitedPoints:
        #print(point.name, end=": ")
        if point != points["Start"]:
            visible = isVisible(robot.currentPoint.coord, point.coord)
            # print(visible)
            if(visible):
                print(point.name)
                visiblePoints.append(point)
                robot.addVisiblePoint(point)
    robot.printVisiblePoints()
    print()

    # moviment("Start",0)


if __name__ == "__main__":
    main()
