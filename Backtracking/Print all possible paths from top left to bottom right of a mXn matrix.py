"""
Input : [[1, 2, 3]
         [4, 5, 6]]

Output :[[1 4 5 6],
         [1 2 5 6],
         [1 2 3 6]]
Moves : Right and Down
-> since we are just moving right and down, these is no chance that we end up in loop hence visited matrix is now required
"""

def travel(i,j,curr,mat,ans):

    if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
        return 

    if i == len(mat)-1 and j == len(mat[0])-1:
        ans.append(curr.copy())
        return 
        
    curr.append(mat[i][j])
    travel(i+1,j,curr,mat,ans)    
    travel(i,j+1,curr,mat,ans)
    curr.pop()

def getPaths(mat):
    i = j = 0
    ans = []
    curr = []
    travel(i,j,curr,mat,ans)
    for list1 in ans:
        list1.append(mat[len(mat)-1][len(mat[0])-1])
    return ans


mat1 = [[1, 2, 3],
       [4, 5, 6]]
mat2 = [[1, 2], 
        [3, 4]]

print(getPaths(mat1))
print(getPaths(mat2))