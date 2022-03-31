class Node:
    def __init__(self, state, parent=None, cost=0):
        self.state = state
        self.name = state.name
        self.parent = parent
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth = parent.depth+1

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
            pathCost += self.cost
            node = node.parent
        print("CUSTO DO CAMINHO: " + str(pathCost))


