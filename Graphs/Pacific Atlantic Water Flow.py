"""
Breaking down the problem :

    Allowed water movement :
        - The water can flow any cell adjacent to the ocean into ocea
        - Water can flow from higher to smaller or equal cell

    What are they asking?
        - When it rains, they want to know the cells from which water can flow to both the oceans

    Our approach :
        We do the opposite, let the water flow from ocean to cells with reverse condition of movement and do multi-source
        BFS
"""


class Solution:

    def bfs(self, heights, queue, visited):


        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:

            currRow, currCol = queue.pop(0)

            for moveRow, moveCol in directions:
                newRow = currRow + moveRow
                newCol = currCol + moveCol

                if newRow < 0 or newRow >= len(heights) or newCol < 0 or newCol >= len(heights[0]):
                    continue

                if (newRow, newCol) in visited:
                    continue

                if heights[newRow][newCol] < heights[currRow][currCol]:
                    continue

                visited.add((newRow, newCol))
                queue.append((newRow, newCol))

        return visited

    def pacificAtlantic(self, heights):

        pacificQueue = []
        atlanticQueue = []

        pacificVisited = set()
        atlanticVisited = set()



        for col in range(len(heights[0])):
            pacificQueue.append((0, col))
            pacificVisited.add((0, col))

            atlanticQueue.append((len(heights) - 1, col))
            atlanticVisited.add((len(heights) - 1, col))

        for row in range(len(heights)):
            pacificQueue.append((row, 0))
            pacificVisited.add((row, 0))

            atlanticQueue.append((row, len(heights[0]) - 1))
            atlanticVisited.add((row, len(heights[0]) - 1))

        self.bfs(heights, pacificQueue, pacificVisited)
        self.bfs(heights, atlanticQueue, atlanticVisited)


        res = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):

                if (i, j) in pacificVisited and (i, j) in atlanticVisited:
                    res.append((i, j))

        return res
