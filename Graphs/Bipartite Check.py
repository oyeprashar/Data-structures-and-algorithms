"""
This is the best possible code! We used the generic m-coloring to do bi-partite.
"""


from collections import defaultdict


class Solution:

    def isBipartitePossible(self, currV, adj, color, V, m):

        if currV == V:
            return True

        for candidate_color in range(m):

            candidate_color_available = True
            for nbr in adj[currV]:

                if color[nbr] == candidate_color:
                    candidate_color_available = False
                    break

            if candidate_color_available:
                color[currV] = candidate_color
                if self.isBipartitePossible(currV + 1, adj, color, V, m):
                    return True
                color[currV] = -1

        return False


    def isBipartite(self, V, edges):
        adj = defaultdict(list)

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        color = [-1] * (V + 1)
        return self.isBipartitePossible(0, adj, color, V, m = 2)
