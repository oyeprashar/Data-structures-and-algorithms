"""
***** Find bridges in the graph *****

    What is a bridge?
    An edge whose removal will cause disconnected components

    A more technical understanding of bridge :
    Lets say we are using DFS to discover the nodes. If there is a back edge that lets me jump back from node N to
    an ancestor Node B, then there is no bridge as there is more than one path. If there is no back edge then there is
    a bridge.


    The problem on GFG:
    The problem is asking us to figure out if there is a bridge between two nodes source and destination in the graph


    Example

                  0
                  |
                  1
                 / \
                2   3
                 \ /
                  4

    - Let's say DFS is running, and current recursion stack is 0 -> 1 -> 2 -> 4 -> 3
    - At 3, we have a nbr 1 which is already visited, but it is not parent of 3 and hence a back edge.
    - But since this nbr 1 is still in the call stack its shortest time is not finalised and only intial time is final
    - We update the shortest time of 3 with the initial time of 1

    - IMP : if a parent's child is connected to some ancestor, the shortest time is update in all the nodes connected in
            this subtree as these nodes can reach the ancestor as well.
"""
from collections import defaultdict

class Solution:

    def isBridgeDFS(self, currV, adj, visited, initialTime, shortestTime, currTime, source, destination, parent):

        visited.add(currV)
        initialTime[currV] = currTime[0]
        shortestTime[currV] = currTime[0]
        currTime[0] += 1

        for nbr in adj[currV]:

            # parent of currV is nbr
            if parent[currV] == nbr:
                continue

            if nbr not in visited:

                parent[nbr] = currV

                if self.isBridgeDFS(nbr, adj, visited, initialTime, shortestTime, currTime, source, destination, parent):
                    return True

                # If my child can reach an earlier node, then I can reach it through my child.
                shortestTime[currV] = min(shortestTime[currV], shortestTime[nbr])

               # bridge detected
                if shortestTime[nbr] > initialTime[currV]:
                    if (nbr == source and currV == destination) or (nbr == destination and currV == source):
                        return True

            # back edge found as we found a node that was already visited and not parent of currV
            else:
                shortestTime[currV] = min(shortestTime[currV], initialTime[nbr])

        return False

    def isBridge(self, V, edges, source, destination):

        adj = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        initialTime = [-1] * V
        shortestTime = [-1] * V
        currTime = [0]
        parent = [-1] * V

        # Handles the disconnected component
        for currV in range(V):
            if currV not in visited and self.isBridgeDFS(currV, adj, visited, initialTime, shortestTime, currTime, source, destination, parent):
                return True


        return False
