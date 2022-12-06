"""
        1) initilize inorder of each vertex
        2) append with vertex with zero inorder in the queue
        3) while queue is not empty
            -> pop element from queue
            -> print it
            -> decrease is children's inorder by 1
            -> append the children who's inorder becomes zero
"""
from collections import defaultdict
class Graph:
    def __init__(self, numofVertices):
        self.vertList = defaultdict(list)
        self.numofVertices = numofVertices

    def addEdge(self, u, v):
        self.vertList[u].append(v) # we are not connecting v -> u because we are using self.numofVertices to find all the vertices

    def topologicalSortBFS(self):
        list1 = [0] * (self.numofVertices)

        # list1 can be renamed to inorderDegreeList
        for vertex in range(self.numofVertices):
            for i in self.vertList[vertex]:
                list1[i] += 1
        queue = []

        for i in range(len(list1)):
            if list1[i] == 0:
                queue.append(i)

        while (len(queue) > 0):
            curr = queue.pop(0)
            print(curr, end=" ")
            for v in self.vertList[curr]:
                list1[v] = list1[v] - 1
                if list1[v] == 0:
                    queue.append(v)

g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topologicalSortBFS()

