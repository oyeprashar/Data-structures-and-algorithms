class Solution:

    def isValid(self, oldI, oldJ, newI, newJ, heights):

        if newI < 0 or newI >= len(heights) or newJ < 0 or newJ >= len(heights[0]):
            return False
        if heights[newI][newJ] < heights[oldI][oldJ]:
            return False

        return True

    def dfs(self, i, j, heights, visited, directions):

        visited[i][j] = True

        for direction in directions:
            iNew = i + direction[0]
            jNew = j + direction[1]

            if self.isValid(i, j, iNew, jNew, heights) and visited[iNew][jNew] == False:
                self.dfs(iNew, jNew, heights, visited, directions)

    def pacificAtlantic(self, heights):

        pacificVisited = []
        atlanticVisited = []

        for i in range(len(heights)):
            pacificRow = []
            atlanticRow = []

            for j in range(len(heights[0])):
                pacificRow.append(False)
                atlanticRow.append(False)

            pacificVisited.append(pacificRow)
            atlanticVisited.append(atlanticRow)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # ******* processing Pacific Ocean *******
        # process row 0 for pacific ocean
        for j in range(len(heights[0])):
            self.dfs(0, j, heights, pacificVisited, directions)

        # process col 0 for pacific ocean
        for i in range(len(heights)):
            self.dfs(i, 0, heights, pacificVisited, directions)

        # ******* processing Atlantic Ocean *******
        for j in range(len(heights[0])):
            self.dfs(len(heights) - 1, j, heights, atlanticVisited, directions)

        for i in range(len(heights)):
            self.dfs(i, len(heights[0]) - 1, heights, atlanticVisited, directions)

        common = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacificVisited[i][j] == True and atlanticVisited[i][j] == True:
                    common.append([i, j])

        return common
