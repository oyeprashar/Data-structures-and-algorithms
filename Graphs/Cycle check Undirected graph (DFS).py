from collections import defaultdict
class Graph:
    def __init__(self,numofVertices):
        self.vertList = defaultdict(list)
        self.numofVertices = numofVertices

    def addEdge(self,u,v):
        self.vertList[u].append(v)

    def cycleUndirectedDFS(self,givenVertex,visited,parent):
        visited.add(givenVertex)

        for nbr in self.vertList[givenVertex]:
            if nbr not in visited:
                parent[nbr] = givenVertex
                cycleMila = self.cycleUndirectedDFS(nbr,visited,parent)
                if cycleMila is True:
                    return True
            else:
                # if visited and parent nhi h matlab yeh loop h
                if parent[nbr] != givenVertex:
                    return True
        return False

    def cycleCheck(self):
        visited = set()
        parent = ['X'] * self.numofVertices
        src = 0
        result = self.cycleUndirectedDFS(src,visited,parent)
        if result is True:
            return "CYCLE DETECTED!"
        else:
            return "NO CYCLE!"
g = Graph(5)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,4)
g.addEdge(4,0)
print(g.cycleCheck())