from __future__ import division
from numpy import *
import sys

from ast import Break
import Point
import Poligon
import Robot
from Node import Node
import numpy as np

# global variables
points = {}
poligons = {}
init = Point


# a partir do caminho dado le um arquivo
# constroi os pontos, os poligonos e as arestas


def readFile(path):
    file = open(path, "r")
    for line in file:
        if (line[0] == "\n"):
            break
        aux = line.split()
        if (line[0].isalpha()):
            points[str(line[0])] = (Point.Point(
                aux[0], float(aux[1]), float(aux[2])))
            points[line[0]].printPoint()

    for line in file:
        if (line[0] == "\n"):
            break
        aux = line.split()
        if (len(line) > 2):
            poligon = Poligon.Poligon(int(aux[0]))
            for i in aux[1:]:
                poligon.AddPoint(points[i])
            for i in range(1, len(aux) - 1):
                poligon.CreateEdge(points[aux[i]], points[aux[i + 1]])
            poligons[poligon.id] = poligon

    line = file.readline()
    aux = line.split()
    start = Point.Point("Start", float(aux[0]), float(aux[1]))
    line = file.readline()
    aux = line.split()
    finish = Point.Point("Finish", float(aux[0]), float(aux[1]))
    points["Start"] = start
    points["Finish"] = finish

    init.Point = start


def perp(a):
    b = empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


# line segment a given by endpoints a1, a2
# line segment b given by endpoints b1, b2
# retorna True se ha interseccao e False caso contrario


def seg_intersect(p1, p2, q1, q2):
    a1 = p1.coord
    a2 = p2.coord
    b1 = q1.coord
    b2 = q2.coord
    da = a2 - a1
    db = b2 - b1
    dp = a1 - b1
    dap = perp(da)
    denom = dot(dap, db)
    num = dot(dap, dp)
    if denom != 0:
        intersect = (num / denom) * db + b1
        if intersect[0] == a2[0] and intersect[1] == a2[1]:
            return False
        if intersect[0] == a1[0] and intersect[1] == a1[1]:
            return False

        if (intersect[0] >= a1[0] and intersect[0] <= a2[0]) or (intersect[0] <= a1[0] and intersect[0] >= a2[0]):
            if (intersect[1] >= a1[1] and intersect[1] <= a2[1]) or (intersect[1] <= a1[1] and intersect[1] >= a2[1]):
                if (intersect[0] >= b1[0] and intersect[0] <= b2[0]) or (
                        intersect[0] <= b1[0] and intersect[0] >= b2[0]):
                    if (intersect[1] >= b1[1] and intersect[1] <= b2[1]) or (
                            intersect[1] <= b1[1] and intersect[1] >= b2[1]):
                        return True
        return False


# diz se o ponto destiny é visivel a partir de origin


def isVisible(origin: Point, destiny: Point):
    for poligon in poligons.values():
        for edge in poligon.edges:
            if edge.p1 != destiny and edge.p2 != destiny:
                intersect = seg_intersect(origin, destiny,
                                          edge.p1, edge.p2)
                if intersect:
                    return False
    return True


# Verifica se dois pontos sao adjacentes
# retorna True se forem e False caso contrário


def verifyIfTwoVerticesAreAdjacent(origin: Point, destiny: Point):
    for edge in poligons[findPoligon(origin)].edges:
        if (origin.name == edge.p1.name and destiny.name == edge.p2.name) or (
                origin.name == edge.p2.name and destiny.name == edge.p1.name):
            return True
    return False


# recebe um ponto de origem rotorna se o destiny é visivel


def findNodes(origin: Point, destiny: Point):
    if destiny.name == "Start":
        return False
    if origin.name == "Start":
        return isVisible(origin, destiny)
    else:
        if itsInTheSamePoligon(origin, destiny):
            return verifyIfTwoVerticesAreAdjacent(origin, destiny)
        else:
            return isVisible(origin, destiny)


# retorna o polígono do ponto


def findPoligon(p1: Point):
    for poligon in poligons.values():
        for point in poligon.points:
            if p1.name == point.name:
                return poligon.id


# verifica se o ponto de destino esta no mesmo póligono que o de destino


def itsInTheSamePoligon(origin: Point, destiny: Point):
    originId = findPoligon(origin)
    destinyId = findPoligon(destiny)
    if originId == destinyId:
        return True
    else:
        return False


# retorna os pontos visiveis de um ponto raiz


def findChildren(vertice: Point):
    visiblePoints = []
    for point in points.values():
        if point != vertice and findNodes(vertice, point):
            visiblePoints.append(point)
            # print(f"{vertice.name} ve {point.name}")
    return visiblePoints


# ITERATIVE DEEPENING SEARCH FUNCTIONS #
def recursiveDLS(node, robot: Robot, limit: int):
    if robot.currentPoint == points["Finish"]:
        return node
    elif limit == 0:
        return 'cutoff'
    else:
        cutoffOcurred = False
        for child in findChildren(robot.currentPoint):
            if robot.isVisited(child) or robot.isCurrentPoint(child):
                continue
            cost = robot.moveToPoint(child)
            result = recursiveDLS(Node(child, node, cost), robot, limit - 1)
            if result == 'cutoff':
                cutoffOcurred = True
            elif result is not None:
                return result
        return 'cutoff' if cutoffOcurred else None


def depthLimitedSearch(robot, limit):
    return recursiveDLS(Node(points["Start"]), robot, limit)


def iterativeDeepeningSearch(robot):
    for depth in range(sys.maxsize):
        # print(f"DEPTH: {depth}")
        robot.restart()
        result = depthLimitedSearch(robot, depth)
        if result != 'cutoff':
            return result


# IDA* FUNCTIONS #

# END OF ITERATIVE DEEPENING FUNCTIONS #

# BFS A* FUNCTIONS #

def bestFirstSearch(robot, f):
    node = Node(points["Start"])
    node.setScore(f(node))
    frontier = {node.name: node}
    explored = set()
    while frontier:
        node = min(frontier.values(), key=lambda k: k.score)
        # print([(node.name,node.score) for node in frontier.values()])
        # print(node.name + " = " + str(node.score))
        del frontier[node.name]
        explored.add(node.state)
        cost = robot.moveToPoint(node.state)
        node.setCost(cost)
        if robot.isCurrentPoint(points["Finish"]):
            return node
        for child in findChildren(robot.currentPoint):
            if not robot.isVisited(child) and child.name not in frontier:
                childNode = Node(child, node)
                childNode.setScore(f(childNode))
                frontier[childNode.name] = childNode
            elif child.name in frontier:
                if f(frontier[child.name]) < frontier[child.name].score:
                    del frontier[child.name]
                    childNode = Node(child, node)
                    childNode.setScore(f(childNode))
                    frontier[childNode.name] = childNode

def f(node):
    pathCost = 0
    while node:
        pathCost += node.cost
        node = node.parent
    return pathCost

def fh(node):
    return f(node) + node.state.DistanceToPoint(points["Finish"])

def main():
    readFile("entrada1.txt")


    # for point in points.values():
    #     lista = findChildren(point)
    #     # for lst in lista:
    #     #     print(lst.name)
    robot = Robot.Robot(points["Start"], points)
    node = iterativeDeepeningSearch(robot)
    node.printPath()
    robot.printVisitedPoints()
    node.printPathCost()

    print("######### Rodar BFS:")
    robot.restart()
    nodeBFS = bestFirstSearch(robot, f)
    nodeBFS.printPath()
    robot.printVisitedPoints()
    nodeBFS.printPathCost()

    print("######## Rodar A*:")
    robot.restart()
    nodeBFS = bestFirstSearch(robot, fh)
    nodeBFS.printPath()
    robot.printVisitedPoints()
    nodeBFS.printPathCost()


if __name__ == "__main__":
    main()
