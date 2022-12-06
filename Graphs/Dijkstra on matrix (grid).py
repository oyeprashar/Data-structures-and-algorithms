global INT_MAX
global n
n = 4
INT_MAX = 3 ** 38


class Solution:

    # <- this returns the minVertex's co-orinates ->
    def minimumVertex(self, distMat, visited):
        minVertexi = 0
        minVertexj = 0
        max1 = INT_MAX
        for i in range(n):
            for j in range(n):
                if distMat[i][j] < max1 and visited[i][j] == False:
                    max1 = distMat[i][j]
                    minVertexi = i
                    minVertexj = j
        return minVertexi, minVertexj

    def minimumCostPath(self, grid):
        for listItem in grid:
            n = len(listItem)
            # <- visited matrix is created with all False ->
        visited = []
        for i in range(n):
            eachRow = []
            for j in range(n):
                eachRow.append(False)
            visited.append(eachRow)
        # <- distMat is created with all values initialized with INT_MAX ->
        distMat = []
        for i in range(n):
            eachRow1 = []
            for j in range(n):
                eachRow1.append(INT_MAX)
            distMat.append(eachRow1)
        distMat[0][0] = grid[0][0]

        drow = [-1, 1, 0, 0]
        dcol = [0, 0, -1, 1]