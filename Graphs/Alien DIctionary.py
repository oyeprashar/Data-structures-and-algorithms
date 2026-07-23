from collections import defaultdict

class Solution:

    def cycleDetectionDirected(self, currV, cycleVisited, currPath, adj):

        cycleVisited.add(currV)
        currPath.add(currV)

        for nbr in adj[currV]:

            if nbr not in cycleVisited:
                if self.cycleDetectionDirected(nbr, cycleVisited, currPath, adj):
                    return True
            else:
                if nbr in currPath:
                    return True

        currPath.remove(currV)
        return False

    def generateGraph(self, words):

        adj = defaultdict(list)

        for i in range(len(words) -1):

            word1 = words[i]
            word2 = words[i + 1]
            diffFound = False

            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    adj[word1[i]].append(word2[i])
                    diffFound = True
                    break

            # is there is no char diff between word1 and word2 and word1 is longer, then it is an invalid ordering
            if diffFound is False and len(word1) > len(word2):
                return None, False

        return adj, True

    def dfsTopologicalSort(self, currV, visited, ordering, adj):

        visited.add(currV)

        for nbr in adj[currV]:
            if nbr not in visited:
                self.dfsTopologicalSort(nbr, visited, ordering, adj)

        ordering.append(currV)

    def findOrder(self, words):

        """
            1. Generate the graph and check the validity of the ordering
            2. Cycle check in the directed graph
            3. Return its topological sorted order
        """

        # Step 1 : Generate the graph and check the validity of the ordering
        adj, isValid = self.generateGraph(words)

        if not isValid:
            return ""

        ordering = []
        visited = set()
        uniqueChars = self.getUniqueChars(words)
        currPath = set()
        cycleVisited = set()

        # Step 2 : Cycle check in the directed graph
        for currV in uniqueChars:
            if currV not in cycleVisited:
                if self.cycleDetectionDirected(currV, cycleVisited, currPath, adj):
                    return ""

        # Step 3 : Return its topological sorted order
        for currV in uniqueChars:
            if currV not in visited:
                self.dfsTopologicalSort(currV, visited, ordering, adj)

        return ordering[::-1]

    def getUniqueChars(self, words):
        uniqueChars = set()
        for word in words:
            for char in list(word):
                uniqueChars.add(char)
        return uniqueChars


s = Solution()
print(s.findOrder(["ab", "cd", "ef", "ad"]))
