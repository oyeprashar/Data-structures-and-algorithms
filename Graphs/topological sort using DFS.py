from collections import defaultdict

class Solution:

    def dfs(self, currNode, visited, adj, arr):
        visited.add(currNode)

        for nbr in adj[currNode]:
            if nbr not in visited:
                self.dfs(nbr, visited, adj, arr)

        arr.append(currNode)

    def topoSort(self, V, edges):
        adj = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)

        arr = []
        visited = set()
        for currNode in range(V):
            if currNode not in visited:
                self.dfs(currNode, visited, adj, arr)

        return arr[::-1]
