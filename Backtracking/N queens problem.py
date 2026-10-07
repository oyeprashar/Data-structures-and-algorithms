"""
Input: n = 4
Output: [[2, 4, 1, 3], [3, 1, 4, 2]]
Explanation: There are 2 possible solutions for n = 4.

    - n * n represents the board
    - We need to place 4 queens on the board such that they are not attacking each other
    - We need all the configurations for the given number of queens and the board

"""



class Solution:

    def isValidConfig(self,row, col, board):

        """
        Conditions:
            1. No other queen in the same row
            2. No other queen in the same col
            3. No other queen in the same dia

        Since we are placing the queens row by row, we need to check the previous above cells
        """

        if row == 0:
            return True

        for i in range(row - 1, -1, -1):

            if board[i][col] is True:
                return False


        for j in range(col - 1, -1, -1):
            if board[row][j] is True:
                return False



        # checking up left diagonally
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:

            if board[i][j] is True:
                return False

            i -= 1
            j -= 1

        # checking up right
        i = row - 1
        j = col + 1

        while i >= 0 and i < len(board) and j >= 0  and j < len(board):

            if board[i][j] is True:
                return False

            i -= 1
            j += 1



        return True



    def placeNQueens(self, row, board, ans):

        if row == len(board):
            ans.append(self.convertToExpectedOutput(board))
            return

        for col in range(len(board[0])):

            if self.isValidConfig(row, col, board):
                board[row][col] = True
                self.placeNQueens(row + 1, board, ans)
                board[row][col] = False

        return


    def convertToExpectedOutput(self, board):
        ans = []
        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] is True:
                    ans.append(j + 1)

        return ans

    def nQueen(self, n):

        board = []
        for i in range(n):
            currRow = []
            for j in range(n):
                currRow.append(False)
            board.append(currRow)

        ans = []
        self.placeNQueens(0, board, ans)

        return ans


s = Solution()
print(s.nQueen(4))