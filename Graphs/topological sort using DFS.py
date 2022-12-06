from collections import defaultdict

class Graph:
    def __init__(self, numofVertices):
        self.vertList = defaultdict(list)
        self.numofVertices = numofVertices

    def addEdge(self, u, v):
        self.vertList[u].append(v)  # we are not connecting v -> u because topological sorting works only on DAG

    def topologicalSortHelper(self, givenVertex, visited, topoList):
        visited.add(givenVertex)

        for v in self.vertList[givenVertex]:
            if v not in visited:
                self.topologicalSortHelper(v, visited, topoList)

        topoList.append(givenVertex)  # yeh recursion ke niche likha h because pehele iss node ko recursively process kr rhe h and jab ho ja rha h process
                                      # tab isse list me append kr de rhe hai
    def topologicalSort(self):
        visited = set()
        topoList = []
        for i in range(self.numofVertices):
            if i not in visited:
                self.topologicalSortHelper(i, visited, topoList)
        print(topoList[::-1])


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topologicalSort()