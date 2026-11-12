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
class Solution:

    def bridgeDetectionDFS(self, currV, adj, initialTimes, shortestTimes, currTime, parent, visited, bridges):

        visited.add(currV)
        initialTimes[currV] = currTime[0]
        shortestTimes[currV] = currTime[0]
        currTime[0] += 1

        for nbr in adj[currV]:

            if nbr not in visited:
                parent[nbr] = currV
                self.bridgeDetectionDFS(nbr, adj, initialTimes, shortestTimes, currTime, parent, visited, bridges)


                """
                So if there is no back edge nbr's shortest time will be greater than currV and since we are picking the min,
                there will be no effect
                
                If there is a back edge we propogate it 
                """
                shortestTimes[currV] = min(shortestTimes[currV], shortestTimes[nbr])

                if shortestTimes[nbr] > initialTimes[currV]:
                    bridges.append([currV, nbr])

            else:
                if parent[currV] == nbr:
                    continue

                """
                We found a node that was already visited and was not the parent of current node
                This means there is a back edge, so initial time of this already visited node is smaller than current V 
                """
                shortestTimes[currV] = min(shortestTimes[currV], initialTimes[nbr])


    def findBridges(self, adj):

        visited = set()
        initialTimes = [0] * len(adj)
        shortestTimes = [0] * len(adj)
        currentTime = [0]
        parent = [-1] * len(adj)
        bridges = []

        for currV in range(len(adj)):

            if currV not in visited:
                self.bridgeDetectionDFS(currV, adj, initialTimes, shortestTimes, currentTime, parent, visited, bridges)

        return bridges


s = Solution()
print(s.findBridges([[1, 2], [0], [0]]))
