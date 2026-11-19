from collections import defaultdict

class Solution:

    def getAdjFromEdges(self, edges):

        adj = defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj

    def detectLoopUndirected(self, currV, adj, visited, parent):

        visited.add(currV)

        for nbr in adj[currV]:

            if nbr not in visited:
                parent[nbr] = currV

                if self.detectLoopUndirected(nbr, adj, visited, parent):
                    return True

            else:
                if parent.get(currV) != nbr: # This will not cause the key error
                    return True

        return False



    def dfs(self, currV, adj, visited):

        visited.add(currV)

        for nbr in adj[currV]:
            if nbr not in visited:
                self.dfs(nbr, adj, visited)


    def countComponents(self, n, adj):


        visited = set()
        componentCount = 0

        for currV in range(n):
            if currV not in visited:
                self.dfs(currV, adj, visited)
                componentCount += 1

        return componentCount


    def validTree(self, n, edges):

        adj = self.getAdjFromEdges(edges)

        if self.countComponents(n, adj) > 1:
            return False

        if self.detectLoopUndirected(0, adj, set(), {}):
            return False



        return True

s = Solution()
print(s.validTree(n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]))
print(s.validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]))
