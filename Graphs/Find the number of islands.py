"""
The time complexity is O(n*m) because even if the whole mat is an island, we explore it once and not for every
iteration of outer nested loops.
"""

class Solution:

    def countNumIslands(self, i, j, grid, directions):

        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return

        if grid[i][j] != "1":
            return

        grid[i][j] = "2"
        for dir in directions:
            self.countNumIslands(i + dir[0], j + dir[1], grid, directions)

    def numIslands(self, grid):

        count = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    self.countNumIslands(i, j, grid, directions)

        return count

grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]

s = Solution()
print(s.numIslands(grid))
