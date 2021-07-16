from collections import defaultdict

global INT_MAX
INT_MAX = 3 ** 38


class Graph:
    def __init__(self):
        self.vertList = defaultdict(list)

    def addEdge(self, u, v):
        self.vertList[u].append(v)

    def distanceBFS(self, src, target):
        queue = [src]
        distanceDict = {}
        for v in self.vertList:
            distanceDict[v] = INT_MAX
        distanceDict[src] = 0
        visited = set()
        visited.add(src)
        while len(queue) > 0:
            curr = queue.pop(0)

            for vertex in self.vertList[curr]:
                if vertex not in visited:
                    queue.append(vertex)
                    visited.add(vertex)
                    distanceDict[vertex] = distanceDict[curr] + 1

        print(distanceDict[target])



    def solveSnakesLadder(self):
        snakeLadderDict = {2: 13, 5: 2, 9: 18, 18: 11, 17: -13, 20: -14, 24: -8, 25: 10, 32: -2, 34: -22}
        # we have 36 boxes --> i
        # we can throw a dice at each of these 36 boxes and it can be from 1 to 6
        # j is new position on the board after throwing a dice
        for i in range(0, 37):
            for dice in range(1, 7):
                j = i + dice
                if j in snakeLadderDict:
                    j += snakeLadderDict[j]
                if j <= 36:
                    self.addEdge(i, j)
        self.distanceBFS(0, 36)


g = Graph()
g.solveSnakesLadder()
