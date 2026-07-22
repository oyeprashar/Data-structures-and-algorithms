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

"""
from collections import defaultdict

class Solution:

    def findBridgesDFS(self, currV, adj, visited, initialTime, shortestTime, currTime, parent, source, destination):

        visited.add(currV)
        initialTime[currV] = currTime[0]
        shortestTime[currV] = currTime[0]
        currTime[0] += 1

        for nbr in adj[currV]:

            # We just came from this nbr to currV
            if nbr == parent[currV]:
                continue

            if nbr not in visited:

                parent[nbr] = currV

				# early return!
				if self.findBridgesDFS(nbr, adj, visited, initialTime, shortestTime, currTime, parent, source, destination):
					return True

				# if there was a back-edge that nbr found, currV can use that back-edge too and hence we update its time
                shortestTime[currV] = min(shortestTime[currV], shortestTime[nbr])


				# No back edge, we need to go through currV to reach nbr and thats a bridge
                if shortestTime[nbr] > initialTime[currV]:

					# Since the question wants use to return true only if the bridge is between these specific nodes
                    if (currV == source and nbr == destination) or (currV == destination and nbr == source):
						return True


			# nbr is already visited and not parent of currV
            # This means back edge to an ancestor!
            else:

				# initial time of nbr because it can still be in the recursive stack
                shortestTime[currV] = min(shortestTime[currV], initialTime[nbr])

		return False

	def isBridge(self, V, edges, source, destination):



        adj = defaultdict(list)

        for edge in edges:
            u = edge[0]
            v = edge[1]
            adj[u].append(v)
            adj[v].append(u)

        initialTime = [-1] * V
        shortestTime = [-1] * V
        currTime = [0]
        parent = [-1] * V
        visited = set()

        for currV in range(V):
            if currV not in visited:
                if self.findBridgesDFS(currV, adj, visited, initialTime, shortestTime, currTime, parent, source, destination):
                    return True

        return False
