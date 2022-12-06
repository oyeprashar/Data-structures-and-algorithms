"""
Implement dijsktra
"""

from collections import defaultdict

class Graph:

    def __init__(self, numOfNodes):
        self.numOfNodes = numOfNodes
        self.adjList = defaultdict(list)

    def addEdge(self, u, v, cost):

        self.adjList[u].append([v, cost])
        self.adjList[v].append([u, cost])

    def getMinUnvisitedNode(self, distance, visited):

        minV = None
        minCost = 3**38

        for node in range(self.numOfNodes):

            if node not in visited and distance[node] < minCost:
                minCost = distance[node]
                minV = node

        return minV, minCost

    def dijsktra(self):

        INT_MAX = 3**38
        distance = [INT_MAX] * self.numOfNodes
        distance[0] = 0
        visited = set()

        for _ in range(self.numOfNodes):

            currV, currCost = self.getMinUnvisitedNode(distance, visited)
            visited.add(currV)

            for nbr, cost in self.adjList[currV]:
                distance[nbr] = min(distance[nbr], distance[currV] + cost)

        return distance

    def bellmanford(self):

        INT_MAX = 3**38
        distance = [INT_MAX] * self.numOfNodes
        distance[0] = 0

        for _ in range(self.numOfNodes):

            for currV in self.adjList:

                for nbr, edgeCost in self.adjList[currV]:
                    distance[nbr] = min(distance[nbr], distance[currV] + edgeCost)


        for currV in self.adjList:

                for nbr, edgeCost in self.adjList[currV]:
                    if distance[currV] + edgeCost < distance[nbr]:
                        print("negative cycle found")
                        return -1

        return distance

graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(1, 2, 8)
graph.addEdge(7, 8, 7)
graph.addEdge(7, 6, 1)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(2, 3, 7)
graph.addEdge(8, 6, 6)
graph.addEdge(6, 5, 2)
graph.addEdge(3, 5, 14)
graph.addEdge(3, 4, 9)
graph.addEdge(5, 4, 10)
print("Result by dijsktra =",graph.dijsktra())
print("Result by bellanford =",graph.bellmanford())
