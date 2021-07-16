####### Directed graph cycle check (DFS)
from collections import defaultdict

class Graph:

    def __init__(self):
        self.vertList = defaultdict(list)

    def addEdge(self, u, v):
        self.vertList[u].append(v)

    def cyclecheckDFS(self, givenVertex, visited, currStack):
        visited.add(givenVertex)
        currStack.append(givenVertex)

        for nbr in self.vertList[givenVertex]:
            if nbr in currStack:
                return True
            else:
                if nbr not in visited:
                    cycleMila = self.cyclecheckDFS(nbr,visited,currStack)
                    if cycleMila is True:
                        return True

        currStack.pop()
        return False

    def cycleCheck(self):
        visited = set()
        currStack = []
        src = 0
        result = self.cyclecheckDFS(src, visited, currStack)
        if result is True:
            return "CYCLE DETECTED!"
        else:
            return "NO CYCLE DETECTED!"


g = Graph()
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(1, 5)
g.addEdge(5, 6)
g.addEdge(4, 2)
print(g.cycleCheck())