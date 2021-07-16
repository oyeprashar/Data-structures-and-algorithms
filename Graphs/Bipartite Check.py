class Graph:
    def __init__(self, numofVertices):
        self.numofVertices = numofVertices
        self.adjacencyMatrix = [[0 for i in range(self.numofVertices)] for j in range(self.numofVertices)]

    def isBipartite(self, src):
        colorArr = [-1] * self.numofVertices
        colorArr[src] = 0
        queue = []
        queue.append(src)

        while len(queue) > 0:
            curr = queue.pop(0)

            # if self loop is present return False
            if self.adjacencyMatrix[curr][curr] == 1:
                return False

            for nbr in range(self.numofVertices):
                # if there is an edge between curr and nbr and nbr is not colored
                if self.adjacencyMatrix[curr][nbr] == 1 and colorArr[nbr] == -1:
                    colorArr[nbr] = 1 - colorArr[curr]
                    queue.append(nbr)

                elif self.adjacencyMatrix[curr][nbr] == 1 and colorArr[nbr] == colorArr[curr]:
                    return False
        return True


g = Graph(4)
g.adjacencyMatrix = [[0, 1, 0, 1],
                     [1, 0, 1, 0],
                     [0, 1, 0, 1],
                     [1, 0, 1, 0]]
print(g.isBipartite(0))

