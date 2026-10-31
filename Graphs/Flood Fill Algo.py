"""
The only catch in flood fill is when the source color and new color both are same and the code get stuck in loop coloring
the same nodes over and over again!
"""

class Solution:

    def floodFillHelper(self, i, j, grid, sourceColor, color, directions, visited):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return

        if grid[i][j] != sourceColor:
            return

        if (i, j) in visited:
            return

        grid[i][j] = color
        visited.add((i, j))

        for moveRow, moveCol in directions:
            self.floodFillHelper(i + moveRow, j + moveCol, grid, sourceColor, color, directions, visited)


    def floodFill(self, image, sr, sc, color):

        """
        The algo never quits when the source color and the new color both are same
        In that case the algo will get stuck in loop coloring the same cells again and again
        """

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        sourceColor = image[sr][sc]
        visited = set()

        self.floodFillHelper(sr, sc, image, sourceColor, color, directions, visited)
        return image