from collections import defaultdict


class Solution:

    def __init__(self):
        self.vertList = defaultdict(list)

    def addEdge(self, u, v):
        self.vertList[u].append(v)

    def topologicalSortDFS(self, givenV, visited, stack):
        visited.add(givenV)

        for nbr in self.vertList[givenV]:
            if nbr not in visited:
                self.topologicalSortDFS(nbr, visited, stack)
        stack.append(givenV)

    def findOrder(self, dict, N, K):
        list1 = dict
        # <- CREATE EDGES ->
        for i in range(len(list1) - 1):
            word1 = list1[i]
            word2 = list1[i + 1]
            rangej = min(len(word1), len(word2))
            for j in range(rangej):
                if word1[j] != word2[j]:
                    u = word1[j]
                    v = word2[j]
                    self.addEdge(u, v)
                    break
        stack = []
        visited = set()
        vlist = [v for v in self.vertList]

        # <- DO TOPOLOGICAL SORT ->
        for v in vlist:
            if v not in visited:
                self.topologicalSortDFS(v, visited, stack)
        result = " ".join(stack[::-1])

        return result
