# is valid function is correct
def isValid(row, col, number, grid):

    # checking the col
    for row1 in range(9):
        if grid[row1][col] == number:
            return False

    # checking the row
    for col1 in range(9):
        if grid[row][col1] == number:
            return False

    startRow = (row // 3) * 3
    startCol = (col // 3) * 3

    for i1 in range(startRow, startRow + 3):
        for j1 in range(startCol, startCol + 3):
            if grid[i1][j1] == number:
                return False

    return True

def SolveSudokuHelper(row, col, grid):
    # print(row, col)

    if row == 9:
        print(grid)
        return

    if col == 9:
        return SolveSudokuHelper(row + 1, 0, grid)

    if grid[row][col] != 0:
        return SolveSudokuHelper(row, col + 1, grid)

    for num in range(1, 10):

        if isValid(row, col, num, grid) is True:
            grid[row][col] = num
            SolveSudokuHelper(row, col + 1, grid)
            grid[row][col] = 0

def SolveSudoku(grid):

    SolveSudokuHelper(0, 0, grid)



grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1 ],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6 ,3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3 ,0, 0, 0, 0 ,2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0 ,6, 3, 0, 0]]


SolveSudoku(grid)

