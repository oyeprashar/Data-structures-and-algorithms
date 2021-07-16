from collections import defaultdict

global INT_MAX
INT_MAX = 3 ** 38


class Graph:
    def __init__(self, numofVertices):
        self.vertList = defaultdict(list)
        self.numofVertices = numofVertices

    def addEdge(self, u, v, cost):
        self.vertList[u].append((v, cost))
        self.vertList[v].append((u, cost))

    def minDist(self, dist, visited):
        max1 = 3 ** 38
        minIndex = 0
        for v in range(self.numofVertices):
            if dist[v] < max1 and v not in visited:
                max1 = dist[v]
                minIndex = v
        return minIndex

    def dijsktra(self, src):
        dist = [INT_MAX] * self.numofVertices
        dist[src] = 0
        visited = set()
        pathDict = defaultdict(list)
        for _ in range(self.numofVertices):
            minVertex = self.minDist(dist, visited)  # min and unvisted

            visited.add(minVertex)
            for nbr, edgeCost in self.vertList[minVertex]:
                if dist[nbr] > dist[minVertex] + edgeCost:
                    if nbr not in visited:
                        dist[nbr] = dist[minVertex] + edgeCost
                        pathDict[src].append((nbr,dist[nbr]))
        return dist

g = Graph(9)
g.addEdge(0, 1, 4)
g.addEdge(0, 7, 8)
g.addEdge(1, 7, 11)
g.addEdge(7, 8, 7)
g.addEdge(7, 6, 1)
g.addEdge(7, 1, 11)
g.addEdge(1, 2, 8)
g.addEdge(2, 3, 7)
g.addEdge(2, 5, 4)
g.addEdge(2, 8, 2)
g.addEdge(6, 8, 6)
g.addEdge(6, 5, 2)
g.addEdge(5, 2, 4)
g.addEdge(5, 3, 14)
g.addEdge(5, 4, 10)
g.addEdge(3, 4, 9)
print(g.dijsktra(0))
