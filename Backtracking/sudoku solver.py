"""
Since we have 9 options at each n*m cells the time complexity is O(9^(n*m))


Box index = boxRow * numberOfBoxesPerRow + boxCol

Where,
    boxRow = row // numberOfRowsInABox
    boxCol = col // numberOfColsInABox

"""

class Solution:

    def isValid(self, num, row, col, rowSet, colSet, boxes):

        """
        Rules :
            1. Same number cannot be in the same row
            2. Same number cannot be in the same column
            3. Same number cannot be in the same 3*3 box
        """

        if num in rowSet[row]:
            return False

        if num in colSet[col]:
            return False

        boxIndex = (row // 3) * 3 + (col // 3)
        if num in boxes[boxIndex]:
            return False

        return True

    def placeNumber(self, num, row, col, rowSet, colSet, boxes, mat):

        mat[row][col] = num
        rowSet[row].add(num)
        colSet[col].add(num)
        boxIndex = (row // 3) * 3 + (col // 3)
        boxes[boxIndex].add(num)


    def unplaceNumber(self, num, row, col, rowSet, colSet, boxes, mat):
        mat[row][col] = 0
        rowSet[row].remove(num)
        colSet[col].remove(num)
        boxIndex = (row // 3) * 3 + (col // 3)
        boxes[boxIndex].remove(num)

    def sudokuSolver(self, row, col, mat, rowSet, colSet, boxes):

        # everything is processed, save
        if row == len(mat):
            # TODO : we have solved the board, save it
            return True

        # all the cols were process, moved to next row
        if col == len(mat[0]):
            return self.sudokuSolver(row + 1, 0, mat, rowSet, colSet, boxes)

        # cell is not empty, move to the next col
        if mat[row][col] != 0:
            return self.sudokuSolver(row, col + 1, mat, rowSet, colSet, boxes)

        for num in range(1, 10):

            if not self.isValid(num, row, col, rowSet, colSet, boxes):
                continue

            self.placeNumber(num, row, col, rowSet, colSet, boxes, mat)

            # Do not un-place the values which eventually led to a solved board!
            if self.sudokuSolver(row, col + 1, mat, rowSet, colSet, boxes):
                return True

            # Remove the values which did not end up returning true
            self.unplaceNumber(num, row, col, rowSet, colSet, boxes, mat)


    def initialiseValueSets(self, mat):

        """
        There needs to be a set for each of the following :
            1. All rows
            2. All cols
            3. All boxes
        """

        rowSet = {0 : set(), 1 : set(), 2 : set(), 3 : set(), 4 : set(), 5 : set(), 6 : set(), 7: set(), 8 : set()}
        colSet = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        boxes = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}

        # now we need to loop through the data and fill these sets


        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if mat[i][j] == 0:
                    continue

                rowSet[i].add(mat[i][j])
                colSet[j].add(mat[i][j])

                boxIndex = (i // 3) * 3 + (j // 3)
                boxes[boxIndex].add(mat[i][j])

        return rowSet, colSet, boxes


    def solveSudoku(self, mat):

        rowSet, colSet,boxes = self.initialiseValueSets(mat)
        self.sudokuSolver(0, 0, mat, rowSet, colSet, boxes)
        return mat


matrix = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0],
]

s = Solution()
s.solveSudoku(matrix)
