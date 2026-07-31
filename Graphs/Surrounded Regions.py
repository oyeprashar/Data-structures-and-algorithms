"""
The core idea to solve this is :
    Os that are surrounded by Xs == Os that are unreachable from the boundary Os
"""


class Solution:


    def dfs(self, i, j, mat, directions):

        if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
            return

        if mat[i][j] != "O":
            return

        mat[i][j] = "S"

        for dir in directions:
            self.dfs(i + dir[0], j + dir[1], mat, directions)


    def solve(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # process the boundary rows
        boundaryRows = [0, len(board) - 1]
        for i in boundaryRows:
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    self.dfs(i, j, board, directions)

        # process the boundary columns
        boundaryCols = [0, len(board[0]) - 1]
        for i in range(len(board)):
            for j in boundaryCols:
                if board[i][j] == "O":
                    self.dfs(i, j, board, directions)

        # process the unreachable nodes <-- these are actually surrounded
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"


        # revert the S flag (whole board because DFS can go under tak!
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "S":
                    board[i][j] = "O"

# Test code

board = [["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]]


for row in board:
    print(row)
s = Solution()
s.solve(board)

print("------------------------")
for row in board:
    print(row)

