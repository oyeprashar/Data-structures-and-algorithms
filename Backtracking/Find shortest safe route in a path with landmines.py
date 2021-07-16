"""
mat =  [[1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
        [1,  0,  1,  1,  1,  1,  1,  1,  1,  1],
        [1,  1,  1,  0,  1,  1,  1,  1,  1,  1],
        [1,  1,  1,  1,  0,  1,  1,  1,  1,  1],
        [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
        [1,  1,  1,  1,  1,  0,  1,  1,  1,  1],
        [1,  0,  1,  1,  1,  1,  1,  1,  0,  1],
        [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
        [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
        [0,  1,  1,  1,  1,  0,  1,  1,  1,  1],
        [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
        [1,  1,  1,  0,  1,  1,  1,  1,  1,  1]]
// Calculate length of the shortest safe route possible from any cell in the first column to any cell in the last column of the matrix 
// We have to avoid landmines and their four adjacent cells (left, right, above and below) as they are also unsafe.
// Length of shortest safe route is 13

-> First step is to process the matrix and mark the unsafe vertices!
land mines are marked with 0
"""

def processMat(mat,visited1):

    for i in range(len(mat)):
        for j in range(len(mat[0])):

            if visited1[i][j] == 1 or mat[i][j] == 1:
                continue

            if i-1 >= 0:        # UP
                mat[i-1][j] = 0
                visited1[i-1][j] = 1

            if i+1 < len(mat):  # Down
                mat[i+1][j] = 0
                visited1[i+1][j] = 1

            if j+1 < len(mat[0]): # Right
                mat[i][j+1] = 0
                visited1[i][j+1] = 1

            if j-1 >= 0:
                mat[i][j-1] = 0
                visited1[i][j-1] = 1

def travel(i,j,mat,count,visited2,minPath):
    if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
        return

    if mat[i][j] == 0 or visited2[i][j] == 1:
        return 

    if j == len(mat[0])-1:
        minPath[0] = min(minPath[0],count)
        return

    visited2[i][j] = 1
    travel(i-1,j,mat,count+1,visited2,minPath)
    travel(i+1,j,mat,count+1,visited2,minPath)
    travel(i,j-1,mat,count+1,visited2,minPath)
    travel(i,j+1,mat,count+1,visited2,minPath)
    visited2[i][j] = 0

def getAns(mat):
    visited1 = []
    for x1 in range(len(mat)):
        list1 = []
        for y1 in range(len(mat[0])):
            list1.append(0)
        visited1.append(list1)

    visited2 = []
    for x2 in range(len(mat)):
        list2 = []
        for y2 in range(len(mat[0])):
            list2.append(0)
        visited2.append(list2)

    processMat(mat,visited1)
    minAns = [3**38]

    for i in range(len(mat)):

        minPath = [3**38]
        travel(i,0,mat,0,visited2,minPath) # from any cell on the index 0 column, so column changes and column remains 0
        minAns[0] = min(minPath[0],minAns[0])  # minPath is the minimum path length from current source cell
                                               # minAns is minimum path length among all the sources we have seen so far
    return minAns[0]




mat =  [[1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
        [1,  0,  1,  1,  1,  1,  1,  1,  1,  1],
        [1,  1,  1,  0,  1,  1,  1,  1,  1,  1],
        [1,  1,  1,  1,  0,  1,  1,  1,  1,  1],
        [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
        [1,  1,  1,  1,  1,  0,  1,  1,  1,  1],
        [1,  0,  1,  1,  1,  1,  1,  1,  0,  1],
        [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
        [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
        [0,  1,  1,  1,  1,  0,  1,  1,  1,  1],
        [1,  1,  1,  1,  1,  1,  1,  1,  1,  1],
        [1,  1,  1,  0,  1,  1,  1,  1,  1,  1]]

print(getAns(mat))





