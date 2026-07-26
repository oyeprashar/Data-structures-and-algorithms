from collections import defaultdict


class Solution:

    def DFS(self, currV, adj, visited):

        visited.add(currV)

        for nbr in adj[currV]:
            if nbr not in visited:
                self.DFS(nbr, adj, visited)


    def makeConnected(self, n, connections):

        # minimum edges needed to connected n nodes is n - 1
        # if the number of edges < n - 1 then it's impossible
        if len(connections) < n - 1:
            return -1

        adj = defaultdict(list)

        for connection in connections:
            u = connection[0]
            v = connection[1]
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        disconnectedComputers = 0

        # One disconnected component is treated as connected, and we don't need cables
        self.DFS(0, adj, visited)

        # All the other components are treated as disconnected from the that main components
        for currV in range(n):
            if currV not in visited:
                self.DFS(currV, adj, visited)
                disconnectedComputers += 1

        return disconnectedComputers
