# <-- IMPORTANT --> BFS can be used to check cycle only in undirected graph
from collections import defaultdict

global INT_MIN
INT_MIN = -3 ** 38


class Graph:

    def __init__(self, numofVertices):
        self.vertList = defaultdict(list)
        self.numofVertices = numofVertices

    def addEdge(self, u, v):
        self.vertList[u].append(v)

    def isTree(self):
        visited = set()
        queue = []
        src = 0  # as graph always starts from zero
        queue.append(src)
        visited.add(src)
        parentList = [INT_MIN] * self.numofVertices
        
        while len(queue) > 0:
            currVertex = queue.pop(0)

            for nbr in self.vertList[currVertex]:
                if nbr in visited and parentList[currVertex] != nbr:
                    return False
                else:
                    parentList[nbr] = currVertex # parentList me index is child and value is parent
                    visited.add(nbr)
                    queue.append(nbr)
        return True

g = Graph(6)
g.addEdge(0, 1)
g.addEdge(3, 2)
g.addEdge(1, 2)
# g.addEdge(0,3)
print(g.isTree())