"""
for _ in range(self.numOfvertics):
    1) Pick the minimum unvisted vertex and add it to path and its cost to totalcost, mark this minvertex as visited
    2) Update the cost of its children
"""
global INT_MAX
INT_MAX = 3 ** 38
from collections import defaultdict


class Graph:
    def __init__(self, numofVertices):
        self.numofVertices = numofVertices
        self.vertList = defaultdict(list)

    def addEdge(self, u, v, edgeCost):
        self.vertList[u].append((v, edgeCost))

    def minDist(self, cost, visited):
        max1 = 3 ** 38
        minVertex = 0
        for v in range(self.numofVertices):
            if cost[v] < max1 and v not in visited:
                max1 = cost[v]
                minVertex = v
        return minVertex,max1

    def prims(self, src):
        cost = [INT_MAX] * self.numofVertices
        cost[src] = 0
        visited = set()
        MSTpath = []
        MSTcost = 0

        for _ in range(self.numofVertices):
            minVertex,costV = self.minDist(cost, visited)  # minVertex changes everytime
            visited.add(minVertex)
            MSTcost += costV
            MSTpath.append(minVertex)

            for nbr, edgeCost in self.vertList[minVertex]:
                if edgeCost < cost[nbr] and nbr not in visited:
                    cost[nbr] = edgeCost
        return MSTpath,MSTcost
g = Graph(4)
g.addEdge(0,1,5)
g.addEdge(0,3,3)
g.addEdge(1,0,5)
g.addEdge(1,2,1)
g.addEdge(2,1,1)
g.addEdge(2,3,2)
g.addEdge(3,0,3)
g.addEdge(3,2,2)
print(g.vertList)
print(g.prims(0))
