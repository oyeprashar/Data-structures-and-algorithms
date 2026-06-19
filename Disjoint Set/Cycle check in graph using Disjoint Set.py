"""
disjoint set

Disjoint sets are sets with nothing in common between them

Find(x) : finds and returns the absolute parent of x --> T.C : O(N)
Union : Merges two disjoint set by making parent of one set equal to another set --> T.C : O(N)

Finding loop in undirected graph using DSU
def findLoopUndirectedGraph(edges):
    for edge in edges:
        parent1 = find(u)
        parent2 = find(v)

        # They were already connected through some other path?
        if parent1 == parent2:
            return true

        union(u, v)
"""

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

def find_undirected_loop(edge_list, number_of_nodes):

    disjoint_set = DisjointSet(number_of_nodes)

    # O(number_of_edges * logN)
    for edge in edge_list:
        u = edge[0]
        v = edge[1]

        parent1 = disjoint_set.find_parent(u)
        parent2 = disjoint_set.find_parent(v)

        if parent1 == parent2:
            return True
        disjoint_set.union(u, v)
    return False

edgeList = [(0,1),(1,2),(2,3),(3,0)]
print(find_undirected_loop(edgeList, number_of_nodes = 4))
