mat =[   ['#','#','#','#','#','#','#','#'],
         ['.','.','#','#','#','#','.','.'],
         ['.','.','#','.','.','#','.','.'],
         ['.','.','#','.','.','#','.','.'],
         ['.','.','#','.','.','#','.','.'],
         ['.','.','#','#','#','#','.','.'],
         ['#','#','#','#','#','#','#','#']]
drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

def floodFill(mat, i, j, nrow, ncolumns, charToBeReplaced, color):
    if i < 0 or j < 0 or i >= nrow or j >= ncolumns:
        return # do nothing

    if mat[i][j] != charToBeReplaced:
        return

    mat[i][j] = color

    for k in range(len(drow)):
        floodFill(mat, i + drow[k], j + dcol[k], nrow, ncolumns, charToBeReplaced, color)

floodFill(mat, 2, 3, 7, 8, '.', 'r')
for listItem in mat:
    print(listItem)


