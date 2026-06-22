"""
Rotate matrix by 90 degrees or find transpose of a matrix
"""

def rotate90(mat):

    # Find the transpose of the matrix
    for i in range(len(mat)):
        for j in range(i + 1, len(mat[0])):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # reverse the rows
    for i in range(len(mat)):
        mat[i] = mat[i][::-1]

    return mat

mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

mat = rotate90(mat)

for row in mat:
    print(row)
    
