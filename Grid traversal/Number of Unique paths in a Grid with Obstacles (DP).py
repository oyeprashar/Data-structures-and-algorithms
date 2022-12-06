# from (0,0) to (m - 1, n - 1) and moving down (right and down) is allowed
def findPaths(i, j, mat, memory):

    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
        return 0

    if mat[i][j] == 1:
        return 0

    if i == len(mat) - 1 and j == len(mat[0]) - 1:
        return 1

    if memory[i][j] != -1:
        return memory[i][j]

    op1 = findPaths(i + 1, j, mat, memory)
    op2 = findPaths(i, j + 1, mat, memory)

    memory[i][j] = op1 + op2
    return memory[i][j]

mat =   [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]

def getTotalPaths(mat):

    memory = []
    for i in range(len(mat)):
        currRow = []
        for j in range(len(mat[0])):
            currRow.append(-1)
        memory.append(currRow)

    return findPaths(0, 0, mat, memory)


print(getTotalPaths(mat))