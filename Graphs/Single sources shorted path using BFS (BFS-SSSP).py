from collections import defaultdict
global INT_MAX
INT_MAX = 3**38
class Graph:
    def __init__(self):
        self.vertices = defaultdict(list)
    def addEdge(self,u,v):
        self.vertices[u].append(v)
        self.vertices[v].append(u)
    def BFS(self,givenVertex):
        queue = []
        distanceDict = {}

        for v in self.vertices:
            distanceDict[v] = INT_MAX

        distanceDict[givenVertex] = 0
        queue.append(givenVertex)
        visited = set()
        visited.add(givenVertex)

        while len(queue)>0:
            curr = queue.pop(0)

            for vertex in self.vertices[curr]:
                if vertex not in visited:
                    visited.add(curr)
                    queue.append(vertex)                            # while calculating distance we need to make it visited then calculate its distance
                    distanceDict[vertex] = distanceDict[curr] + 1   # this ensures that the distance is not calculated again
                    
        print(distanceDict)

g = Graph()     # {0: 0, 1: 1, 3: 1, 2: 2, 4: 2, 5: 3}
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(1,0)
g.addEdge(2,3)
g.addEdge(2,1)
g.addEdge(3,2)
g.addEdge(3,0)
g.addEdge(3,4)
g.addEdge(4,5)
g.addEdge(5,4)
g.BFS(0)