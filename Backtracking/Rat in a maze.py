"""
-> Rat can move in directions - Up,Down,Right,Left
-> Rat can only travel through cells having 1
-> Rat cannot travel throught cells having 0
-> Rat cannot revisit the cell it visited in the current path
"""

class Solution:

    def findPaths(self, i, j, grid, destination, directions, currPath, res):


        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return

        if grid[i][j] == 0 or grid[i][j] == 2:
            return

        # if destination, save the path in the res
        if i == len(grid) - 1 and j == len(grid[0]) - 1:
            res.append("".join(currPath))
            return

        grid[i][j] = 2

        for moveRow, moveCol, direction in directions:

            currPath.append(direction)
            self.findPaths(i + moveRow, j + moveCol, grid, destination, directions, currPath, res)
            currPath.pop()

        grid[i][j] = 1


    def ratInMaze(self, maze):

        # if the source or destination is blocked, it makes no sense to make recursive calls
        if maze[0][0] == 0 or maze[len(maze) - 1][len(maze[0]) - 1] == 0:
            return []

        destination = [len(maze) - 1, len(maze[0]) - 1]
        directions = [( -1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]

        res = []
        self.findPaths(0, 0, maze, destination, directions, [], res)
        return sorted(res)

s = Solution()
maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]]

print(s.ratInMaze(maze))