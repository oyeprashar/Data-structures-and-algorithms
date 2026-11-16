"""
The board starts from the last row and then alternates and that is why we have such logic in getCellIndex

                                        [[36,  35,  34,  33,  32,  31],
                                        [25,   26,  27,  28,  29,  30],
                                        [24,   23,  22,  21,  20,  19],
                                        [13,   14,  15,  16,  17,  18],
                                        [12,   11,  10,  9,   8,   7],
                                        [1,     2,   3,  4,   5,   6]]

"""


class Solution:

    def getCellIndex(self, cellNumber, boardSize):

        """
        Logic for row : // n removes the factor of n from cellNumber telling how many rows we have passed and effectively where we re
        Logic for col : % modulo gives the remainder, when we do % n it tells how many positions are remaining to be filled in that row

        """

        row = (boardSize - ((cellNumber) - 1) // boardSize) - 1
        col = (cellNumber - 1) % boardSize

        # The bottom row is the first row thats is why we are using this logic to flip rows from l->r to r -> l
        if row % 2 == boardSize % 2:
            col = boardSize - 1 - col

        return row, col


    ## TODO : Check if the 1 based or 0 based indexing is an issue here
    def getPotentialCellList(self, currCell, boardSize):
        return list(range(currCell + 1, min(currCell + 6, boardSize * boardSize) + 1))


    def snakesAndLadders(self, board):
        """
        We need to return back the minimum number dice roll needed to reach n * n cell
        The dice roll w
        """
        queue = []
        queue.append(1)
        levels = 0
        targetCell = len(board) ** 2
        visited  = set()
        visited.add(1)

        while queue:

            for _ in range(len(queue)):
                currCellNumber = queue.pop(0)
                newCells = self.getPotentialCellList(currCellNumber, len(board))

                for cellNumber in newCells:

                    row, col = self.getCellIndex(cellNumber, len(board))
                    if board[row][col] != -1:
                        cellNumber = board[row][col]

                    if cellNumber in visited:
                        continue

                    if cellNumber >= targetCell:
                        return levels + 1

                    queue.append(cellNumber)
                    visited.add(cellNumber)

            levels += 1

        return -1


s = Solution()
print(s.snakesAndLadders(board = [[-1,-1],[-1,3]]))