def findMaxDiff(mat):

    memory = []

    for x in range(len(mat)):
        list1 = []
        for y in range(len(mat[0])):
            list1.append(0)
        memory.append(list1)
    
    # preprocess the last row

    maxVal = mat[-1][-1]
    memory[-1][-1] = maxVal

    for col in range(len(mat[0])-2,-1,-1):

        maxVal = max(maxVal,mat[len(mat)-1][col])

        memory[len(mat)-1][col] = maxVal

    # preprocess the last col

    maxVal = mat[-1][-1]

    for row in range(len(mat)-2,-1,-1):

        maxVal = max(maxVal,mat[row][len(mat[0])-1])

        memory[row][len(mat[0])-1] = maxVal

    
    n = len(mat)
    m = len(mat[0])
    maxDiff = -3**38

    for i in range(n-2,-1,-1):
        for j in range(m-2,-1,-1):
            
            currDiff = memory[i+1][j+1] - mat[i][j]

            maxDiff = max(maxDiff,currDiff)

            memory[i][j] = max(mat[i][j],memory[i+1][j],memory[i][j+1])
        
    return maxDiff

    
mat =       [[ 1, 2, -1, -4, -20 ],
             [ -8, -3, 4, 2, 1 ], 
             [ 3, 8, 6, 1, 3 ],
             [ -4, -1, 1, 7, -6 ],
             [ 0, -4, 10, -5, 1 ]]


print(findMaxDiff(mat))