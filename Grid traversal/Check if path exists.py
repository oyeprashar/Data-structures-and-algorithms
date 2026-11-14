class Solution:

    def findSourceCoordinates(self, mat):

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if mat[i][j] == 1:
                    return i, j

        return None, None

    def BFSPathFinder(self, sourceRow, sourceCol, mat):

        queue = [(sourceRow, sourceCol)]
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()
        visited.add((sourceRow, sourceCol))

        while queue:

            currRow, currCol = queue.pop(0)
            for moveRow, moveCol in directions:

                newRow, newCol = currRow + moveRow, currCol + moveCol

                if newRow < 0 or newRow >= len(mat) or newCol < 0 or newCol >= len(mat[0]):
                    continue

                if mat[newRow][newCol] == 0 or (newRow, newCol) in visited:
                    continue

                if mat[newRow][newCol] == 2:
                    return True

                visited.add((newRow, newCol))
                queue.append((newRow, newCol))

        return False

    def isPathPossible(self, mat):

        sourceRow, sourceCol = self.findSourceCoordinates(mat)

        if sourceRow is None or sourceCol is None:
            return False

        return self.BFSPathFinder(sourceRow, sourceCol, mat)