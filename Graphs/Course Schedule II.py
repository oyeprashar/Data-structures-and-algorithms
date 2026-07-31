
from collections import defaultdict

class Solution:


    def detectCycleDirectedGraph(self, currV, visited, adj, currPath):

        visited.add(currV)
        currPath.add(currV)

        for nbr in adj[currV]:

            if nbr not in visited:
                if self.detectCycleDirectedGraph(nbr, visited, adj, currPath):
                    return True

            else:
                if nbr in currPath:
                    return True

        currPath.remove(currV)
        return False


    def finishOrderDFS(self, currV, visited, adj, ordering):

        visited.add(currV)

        for nbr in adj[currV]:
            if nbr not in visited:
                self.finishOrderDFS(nbr, visited, adj, ordering)

        ordering.append(currV)


    def findOrder(self, numCourses, prerequisites):

        adj = defaultdict(list)

        ### TODO : This is the weirdest part of the problem! [a, b] and the edge is from b -> a
        for edge in prerequisites:
            u = edge[1]
            v = edge[0]
            adj[u].append(v)

        # check for cycle
        visitedCycle = set()
        currPath = set()
        for currV in range(numCourses):
            if currV not in visitedCycle:
                if self.detectCycleDirectedGraph(currV, visitedCycle, adj, currPath):
                    print("cycle detected")
                    return []

        # topological sort
        visited = set()
        ordering = []
        for currV in range(numCourses):
            if currV not in visited:
                self.finishOrderDFS(currV, visited, adj, ordering)


        return ordering[::-1]