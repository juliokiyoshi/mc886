class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.name = state.name
        self.parent = parent
        self.cost = cost
        self.score = 0

    def printPath(self):
        node = self
        nodeList = []
        while node:
            nodeList[:0] = [node]
            node = node.parent
        print("CAMINHO ENCONTRADO:")
        for node in nodeList:
            if node.name == "Finish":
                print(node.name)
            else:
                print(node.name + "->", end="")

    def printPathCost(self):
        node = self
        pathCost = 0
        while node:
            print(f"node {self.name} = {self.cost}, parent {self.parent}")
            pathCost += self.cost
            node = node.parent
        print("CUSTO DO CAMINHO: " + str(pathCost))

    def setScore(self, score):
        self.score = score

    def setCost(self, cost):
        self.cost = cost


