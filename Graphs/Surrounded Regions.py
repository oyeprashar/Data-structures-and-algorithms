"""
The surrounded regions are Os that cannot be reached from the boundary Os so we do BFS from the boundary Os and
mark the unvisited Os are Xs !

TC : O(N*M) because this is simply multiple-source BFS
"""

class Solution:
    def solve(self, board):

        queue = []
        visited = set()
        lastRow = len(board) - 1
        lastCol = len(board[0]) - 1

        for col in range(len(board[0])):
            if board[0][col] == "O":
                queue.append((0, col))
                queue.append((lastRow, col))
                visited.add((0, col))
                visited.add((lastRow, col))

        for row in range(len(board)):
            if board[row][0] == "O":
                queue.append((row, 0))
                queue.append((row, lastCol))
                visited.add((row, 0))
                visited.add((row, lastCol))

        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while queue:

            currRow, currCol = queue.pop(0)

            for moveRow , moveCol in directions:

                newRow = currRow + moveRow
                newCol = currCol + moveCol

                if newRow < 0 or newRow >= len(board) or newCol < 0 or newCol >= len(board[0]):
                    continue

                if (newRow, newCol) in visited:
                    continue

                if board[newRow][newCol] != "O":
                    continue

                visited.add((newRow, newCol))
                queue.append((newRow, newCol))

        for i in range(len(board)):
            for j in range(len(board[0])):

                if (i, j) not in visited and board[i][j] == "O":
                    board[i][j] = "X"

        return board
