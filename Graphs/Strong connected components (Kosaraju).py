from collections import defaultdict


class Graph:
    def __init__(self, numofVertices):
        self.numofVertices = numofVertices
        self.vertList = defaultdict(list)

    def addEdge(self, u, v):
        self.vertList[u].append(v)

    def reverseGraph(self):
        g1 = Graph(self.numofVertices)
        for v in self.vertList:
            for nbr in self.vertList[v]:
                g1.addEdge(nbr, v)
        return g1

    def finishedTimeDFS(self, v, visited1, stack):
        visited1.add(v)
        for nbr in self.vertList[v]:
            if nbr not in visited1:
                self.finishedTimeDFS(nbr, visited1, stack)
        stack.append(v)

    def DFS(self, vertex, visited2):
        visited2.add(vertex)
        print(vertex)
        for nbr in self.vertList[vertex]:
            if nbr not in visited2:
                self.DFS(nbr, visited2)

    def getSCC(self):
        stack = []
        visited1 = set()
        # step1 -> get a stack of finishedTimeDFS ordering
        for i in range(self.numofVertices):
            if i not in visited1:
                self.finishedTimeDFS(i, visited1, stack)
        # step2 -> create a reverse of the graph
        gReversed = self.reverseGraph()

        visited2 = set()
        print("COMPONENTS ARE")
        # step3 -> pop elements from the stack and do a normal DFS traversal using the element as source

        while len(stack) > 0:
            curr = stack.pop()
            if curr not in visited2:
                gReversed.DFS(curr, visited2)
                print(" ")


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(0, 2)
g.addEdge(2, 1)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.getSCC()