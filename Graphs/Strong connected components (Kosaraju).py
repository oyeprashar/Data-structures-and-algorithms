"""
**** Finding SCC using Kosaraju ****

    Algorithm
        1. Find the finish order DFS ordering and reverse this ordering
        2. Reverse the graph
        3. do normal DFS on the finish time ordering and save the scc

    Time complexity is O(V+E) because effectively are just traversing the graph
"""

from collections import defaultdict


class Solution:

    def finishTimeDFS(self, currV, visited, adj, ordering):

        visited.add(currV)

        for nbr in adj[currV]:
            if nbr not in visited:
                self.finishTimeDFS(nbr, visited, adj, ordering)

        ordering.append(currV)

    def kosarajuDFS(self, currV, visited, adj, scc):

        visited.add(currV)
        scc.append(currV)

        for nbr in adj[currV]:
            if nbr not in visited:
                self.kosarajuDFS(nbr, visited, adj, scc)


    def kosaraju(self, V, edges):

        adj, reversedAdj = self.generateGraphAndReverse(edges)

        # step 1 : find the finish time ordering using DFS
        reversedFinishTimeOrdering = self.getReversedFinishtimeDFS(V, adj)

        # step 2 : reverse graph
        # we already did this when we generated the adj


        # step 3 : now we use the finish time ordering to do dfs on reserved graph and find scc
        allSCCs = []
        visited = set()
        for currV in reversedFinishTimeOrdering:
            if currV not in visited:
                scc = []
                self.kosarajuDFS(currV, visited, reversedAdj, scc)
                allSCCs.append(scc)

        return len(allSCCs)

    def generateGraphAndReverse(self, edges):
        adj = defaultdict(list)
        reversedAdj = defaultdict(list)
        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            reversedAdj[v].append(u)
        return adj, reversedAdj

    def getReversedFinishtimeDFS(self, V, adj):
        finishTimeOrdering = []
        visited = set()
        for currV in range(V):
            if currV not in visited:
                self.finishTimeDFS(currV, visited, adj, finishTimeOrdering)
        finishTimeOrdering = finishTimeOrdering[::-1] ### IMP : We reverse the finish time ordering
        return finishTimeOrdering