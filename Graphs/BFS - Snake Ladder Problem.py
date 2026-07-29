class Solution:

    def getCellIndex(self, cellNumber, n):

        row = n - ((cellNumber - 1) // n) - 1
        col = (cellNumber - 1) % n

        if row % 2 == n % 2:
            col = n - 1 - col

        return row, col


    def snakesAndLadders(self, board):

        queue = [1]
        visited = set()
        visited.add(1)
        levels = 0
        n = len(board)
        targetCell = n * n

        while len(queue):

            levels += 1

            for _ in range(len(queue)):

                currentCellNum = queue.pop(0)

                for diceRoll in range(1, 7):

                    newCellNumber = currentCellNum + diceRoll
                    rowIndex, colIndex = self.getCellIndex(newCellNumber, n)

                    # check for snake / ladder
                    if board[rowIndex][colIndex] != -1:
                        newCellNumber = board[rowIndex][colIndex]

                    if newCellNumber >= targetCell:
                        return levels

                    if newCellNumber not in visited:
                        visited.add(newCellNumber)
                        queue.append(newCellNumber)

        return -1
