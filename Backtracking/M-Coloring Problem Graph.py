from collections import defaultdict


class Solution:

    def isColoringPossible(self, currV, adj, m, color, v):

        if currV == v:
            return True

        # we will try all the colors for the current node
        for candidate_color in range(m):

            # check if the nbrs are not using this color
            color_available = True
            for nbr in adj[currV]:
                if color[nbr] == candidate_color:
                    color_available = False
                    break

            # if the color is available, use it!
            if color_available:
                color[currV] = candidate_color
                if self.isColoringPossible(currV + 1, adj, m, color, v): # move ahead to other nodes
                    return True

                color[currV] = -1 # uncolor to try other colors

        return False

    def graphColoring(self, V, edges, m):

        adj = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)

        color = [-1] * (V + 1)

        return self.isColoringPossible(0, adj, m, color, V)
