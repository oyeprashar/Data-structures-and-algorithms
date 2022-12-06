"""
Input:
1 2 3 
4 5 6
7 8 9  
Output:
7 4 1 
8 5 2
9 6 3

Input:
1 2
3 4
Output:
3 1
4 2 
"""

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
    
def rotate90(mat):

    getTranspose(mat)

    for row in range(len(mat)):
        mat[row] = mat[row][::-1]
    
    for list1 in mat:
        print(list1)

    
# mat = [[ 'a','b','c','d'],
        # ['e','f','g','h'],
        # ['i','j','k','l'],
        # ['m','n','o','p']]
        

mat =   [[1, 2, 3], 
        [4, 5, 6],
        [7, 8, 9]] 

        # [[1, 4, 7], 
        # [2, 5, 8], 
        # [3, 6, 9]]

rotate90(mat)

