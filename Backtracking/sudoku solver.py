"""
Since we have 9 options at each n*m cells the time complexity is O(9^(n*m))

Logic to find the index of the box
((box_row * 3) + box_col) = [0, 8]

"""

class Solution:

    def isValidPlacement(self, mat, number, row, col, boxes, rows, cols):

        if mat[row][col] != 0:
            return False

        # if number in the same row
        if number in rows[row]:
            return False

        # if number in the same col
        if number in cols[col]:
            return False

        # if number is already in the same box
        boxIndex = ((row // 3) * 3 + (col // 3))
        if number in boxes[boxIndex]:
            return False

        return True


    def sudokuSolver(self, mat, row, col, boxes, rows, cols):

        if row == len(mat):
            print("**-----Solution found!-----**")
            for row in mat:
                print(row)
            print("-----------------------------")
            return

        # if we have processed the complete row move on to the next row
        if col == len(mat[0]):
            return self.sudokuSolver(mat, row + 1, 0, boxes, rows, cols)

        # if the current cell is not empty, move on to the next cell
        if mat[row][col] != 0:
            return self.sudokuSolver(mat, row, col + 1, boxes, rows, cols)

        for i in range(1, 10):
            if self.isValidPlacement(mat, i, row, col, boxes, rows, cols):
                mat[row][col] = i

                # add
                boxIndex = boxIndex = ((row // 3) * 3 + (col // 3))
                boxes[boxIndex].add(i)
                rows[row].add(i)
                cols[col].add(i)


                self.sudokuSolver(mat, row, col + 1, boxes, rows, cols)

                # remove
                mat[row][col] = 0
                boxes[boxIndex].remove(i)
                rows[row].remove(i)
                cols[col].remove(i)


    def getInitializedDicts(self, mat):

        boxes = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        rows = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}
        cols = {0: set(), 1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set()}

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if mat[i][j] != 0:

                    boxIndex = ((i // 3) * 3) + j // 3
                    boxes[boxIndex].add(mat[i][j])
                    rows[i].add(mat[i][j])
                    cols[j].add(mat[i][j])

        return boxes, rows, cols


    def solveSudoku(self, mat):

        boxes, rows, cols = self.getInitializedDicts(mat)
        self.sudokuSolver(mat, 0, 0, boxes, rows, cols)



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
