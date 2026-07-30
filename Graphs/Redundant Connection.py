
class DisjointSet:

    def __init__(self, size):
        self.parent = [-1] * (size + 1)
        self.rank = [1] * (size + 1)

    # TC : O(logn) because of path compression using rank
    def findParent(self, element):

        if self.parent[element] == -1:
            return element

        return self.findParent(self.parent[element])

    # TC : O(logn) because it uses findParent and does O(1) operations
    def union(self, element1, element2):
        parent1 = self.findParent(element1)
        parent2 = self.findParent(element2)

        rank1 = self.rank[parent1]
        rank2 = self.rank[parent2]

        # parent of element2 becomes element1
        if rank1 > rank2:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]


class Solution:

    def findNumberOfNodes(self, edges):

        maxN = 0

        for edge in edges:
            u = edge[0]
            v = edge[1]
            maxN = max(maxN, u)
            maxN = max(maxN, v)

        return maxN


    def findRedundantConnection(self, edges):

        n = self.findNumberOfNodes(edges)
        dsu = DisjointSet(size=n)


        # O(e * logv)
        for edge in edges:

            u = edge[0]
            v = edge[1]

            parent1 = dsu.findParent(u)
            parent2 = dsu.findParent(v)

            if parent1 == parent2:
                return edge
            else:
                dsu.union(parent1, parent2)

        return []
