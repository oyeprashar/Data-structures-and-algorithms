"""
A graph is a tree is all nodes are reachable (no disconnected components) and there are no loops
"""

from collections import defaultdict

class Solution:

    def DFSCycleCheckUndirected(self, currV, visited, parent, adj):

        visited.add(currV)

        for nbr in adj[currV]:

            if nbr in visited:
                if parent[currV] != nbr:
                    return True

            else:
                parent[nbr] = currV
                if self.DFSCycleCheckUndirected(nbr, visited, parent, adj):
                    return True

        return False

    def dfs(self, currV, visited, adj):

        visited.add(currV)

        for nbr in adj[currV]:
            if nbr not in visited:
                self.dfs(nbr, visited, adj)

    def isTree(self, V, m, edges):

        adj = defaultdict(list)
        for edge in edges:

            u = edge[0]
            v = edge[1]

            adj[u].append(v)
            adj[v].append(u)


        parent = [-1] * V
        cycleVisited = set()
        for currV in range(V):
            if currV not in cycleVisited and self.DFSCycleCheckUndirected(currV, cycleVisited, parent, adj):
                return 0

        visited = set()
        numberOfComponents = 0

        for currV in range(V):

            if currV not in visited:
                self.dfs(currV, visited, adj)
                numberOfComponents += 1
                if numberOfComponents > 1:
                    return 0

        return 1

s = Solution()
print(s.isTree(V = 4, m = 3, edges = [[0, 1], [1, 2], [1, 3]]))
