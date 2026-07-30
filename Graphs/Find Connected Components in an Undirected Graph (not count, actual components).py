from collections import defaultdict

class Solution:

    def DFS(self, currV, visited, adj, component):

        visited.add(currV)
        component.append(currV)
        for nbr in adj[currV]:
            if nbr not in visited:
                self.DFS(nbr, visited, adj, component)

    def getComponents(self, V, edges):

        adj = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)


        visited = set()
        components = []

        for currV in range(V):
            if currV not in visited:
                component = []
                self.DFS(currV, visited, adj, component)
                components.append(component)

        return components


s = Solution()

# Expected Output: [[0, 1, 2], [3, 4]]
print(s.getComponents(V = 5, edges=[[0, 1], [2, 1], [3, 4]]))
