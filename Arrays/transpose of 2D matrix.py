def getTranspose(mat):

    starti = 0
    startj = 0

    while startj < len(mat[0]):

        i = starti 
        j = startj 

        while j < len(mat[0]):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

            j += 1
            i += 1
        
        startj += 1

matrix = [[1,2,3],[4,5,6],[7,8,9]]
getTranspose(matrix)

for list1 in matrix:
    print(list1)
