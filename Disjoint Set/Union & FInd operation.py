class DisjointSet:

    def __init__(self, number_of_nodes):
        self.rank = [1]  * number_of_nodes
        self.parent = [-1] * number_of_nodes

    # Since rank is making the DS balanced the tc of find is O(logN) | Height of tree ≤ O(log N)
    def find_parent(self, node):
        if self.parent[node] == -1:
            return node
        return self.find_parent(self.parent[node])

    # O(log N) since it is finding the parent and then changing the parent in O(1)
    def union(self, node1, node2):
        parent1 = self.find_parent(node1)
        parent2 = self.find_parent(node2)
        rank1 = self.rank[parent1]
        rank2 = self.rank[parent2]

        if rank1 > rank2:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]