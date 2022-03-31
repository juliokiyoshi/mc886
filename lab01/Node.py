class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.name = state.name
        self.parent = parent
        self.depth = 0
        if parent:
            self.depth = parent.depth+1

