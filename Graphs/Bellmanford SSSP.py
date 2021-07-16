from collections import defaultdict

global INT_MAX
INT_MAX = 3 ** 38


class Graph:
    def __init__(self, numofVertices):
        self.edgeList = []
        self.numofVertices = numofVertices

    def addEdge(self, u, v, cost):
        self.edgeList.append((u, v, cost))

    def bellmanFord(self, src):
        dist = [INT_MAX] * self.numofVertices
        dist[src] = 0
        for _ in range((self.numofVertices) - 1):
            for tuple_ in self.edgeList:
                u = tuple_[0]
                v = tuple_[1]
                wt = tuple_[2]

                if dist[v] > dist[u] + wt:
                    dist[v] = dist[u] + wt
        return dist


g = Graph(5)
g.addEdge(0, 1, -1)
g.addEdge(0, 2, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 2)
g.addEdge(1, 4, 2)
g.addEdge(3, 2, 5)
g.addEdge(3, 1, 1)
g.addEdge(4, 3, -3)
print(g.bellmanFord(0))