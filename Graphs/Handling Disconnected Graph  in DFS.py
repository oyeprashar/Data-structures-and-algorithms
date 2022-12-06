from collections import defaultdict


class Graph:
    def __init__(self):
        self.vertices = defaultdict(list)

    def addEdge(self, from_vertex, to_vertex):
        self.vertices[from_vertex].append(to_vertex)
        self.vertices[to_vertex].append((from_vertex))

    def DFS(self):
        visited = set()
        for currVertex in self.vertices:
            if currVertex not in visited:
                self.DFSHelper(currVertex, visited)

    def DFSHelper(self, v, visited):
        visited.add(v)
        print(v, end=" ")

        for vertex in self.vertices:
            if vertex not in visited:
                self.DFSHelper(vertex, visited)


g = Graph()
g.addEdge(0, 1)  # 0 1 2 3
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.DFS()