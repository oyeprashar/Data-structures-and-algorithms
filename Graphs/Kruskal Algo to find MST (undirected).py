"""
KRUSKAL ALGO
>> sort the edges in ascending order
>> keep on adding cost of the edges until loop is not forming
"""
class Graph:
    def __init__(self, numofVertices):
        self.numofVertices = numofVertices
        self.edgeList = []
        self.parentList = [-1] * self.numofVertices
        self.rank = [1] * self.numofVertices

    def addEdge(self, u, v, cost):
        self.edgeList.append((cost, u, v))

    def find(self, element):
        if self.parentList[element] == -1:
            return element
        self.parentList[element] = self.find(self.parentList[element])
        return self.parentList[element]

    def union(self, item1, item2):
        parent1 = self.find(item1)
        parent2 = self.find(item2)

        if parent1 != parent2:
            if self.rank[parent1] < self.rank[parent2]:
                self.parentList[parent1] = parent2
                self.rank[parent2] += self.rank[parent1]
            else:
                self.parentList[parent2] = parent1
                self.rank[parent1] += self.rank[parent2]

    def kruskal(self):
        sortedEdgeList = sorted(self.edgeList)
        minimumCost = 0

        # WE PROCESS ALL THE TUPLES!
        # join the edge if it doesn't form a loop
        for tuple_ in sortedEdgeList:
            if self.find(tuple_[1]) != self.find(tuple_[2]):
                self.union(tuple_[1], tuple_[2])
                minimumCost += tuple_[0]

        return minimumCost


g = Graph(4)
g.addEdge(0, 1, 1)
g.addEdge(1, 3, 3)
g.addEdge(3, 2, 4)
g.addEdge(2, 0, 2)
g.addEdge(0, 3, 2)
g.addEdge(1, 2, 2)
print(g.kruskal())