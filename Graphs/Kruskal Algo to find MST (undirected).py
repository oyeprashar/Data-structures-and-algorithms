"""
***** Kruskal MST Algo (greedy) *****

Algorithm
    1. sort the edges based on the weights in ascending order
    2. loop through these and pick the edges that are not forming loop (use DSU to check loops)
    3. return the total cost once we have N - 1 edges
"""

class DisjointSet:

    def __init__(self, size):
        self.parent = [-1] * size
        self.rank = [1] * size

    # O(logn) because of path compression through rank
    def findParent(self, element):

        if self.parent[element] == -1:
            return element

        return self.findParent(self.parent[element])

    def union(self, element1, element2):

        parent1 = self.findParent(element1)
        parent2 = self.findParent(element2)

        if parent1 == parent2:
            return

        rank1 = self.rank[parent1]
        rank2 = self.rank[parent2]

        # parent of smaller rank is the guy with bigger rank
        if rank1 > rank2:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]

        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]

class Solution:
    def kruskalsMST(self, V, edges):

        # O(eloge)
        edges.sort(key = lambda x:x[2])
        numberOfMerges = 0
        cost = 0
        dsu = DisjointSet(V)

        # O(eloge)
        for edge in edges:

            u = edge[0]
            v = edge[1]
            edgeCost = edge[2]

            parent1 = dsu.findParent(u)
            parent2 = dsu.findParent(v)

            if parent1 != parent2:
                dsu.union(parent1, parent2)
                cost += edgeCost
                numberOfMerges += 1

            if numberOfMerges == V - 1:
                return cost

        return cost
