"""
Implement bellman-ford

Difference in Dijkstra and Bellman-Ford

    * Dijkstra

        for _ in range(V):
            1. Pick the min unvisited node, mark it visited
            2. Relax its nbrs

    * Bellman-Ford

        for _ in range(V - 1):
            for edge in edges:
                relax

        # and use the one pass to detect neg cycle if weights are still decrease
        for edge in edges:
                relax
"""
INT_MAX = 3 ** 38

class Solution:


    def bellmanFord(self, V, edges, src):
        # code here

        dist = [INT_MAX] * V
        dist[src] = 0

        for _ in range(V - 1):

            for edge in edges:

                u = edge[0]
                v = edge[1]
                edgeCost = edge[2]

                """
                if dist[u] == INT_MAX, it means node u is not reachable (atleast yet),
                relaxing V will make it wrong if the edge weight is negative
                """
                if dist[u] != INT_MAX and dist[u] + edgeCost < dist[v]:
                    dist[v] = dist[u] + edgeCost

        for edge in edges:

            u = edge[0]
            v = edge[1]
            edgeCost = edge[2]

            if dist[u] != INT_MAX and dist[u] + edgeCost < dist[v]:
                return "Negative Cycle Found"

        return dist
