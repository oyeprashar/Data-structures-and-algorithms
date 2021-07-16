"""
-> Rat can move in directions - Up,Down,Right,Left
-> Rat can only travel through cells having 1
-> Rat cannot travel throught cells having 0
-> Rat cannot revisit the cell it visited in the current path
"""

def dfs(i,j,mat,s,ansList,visited):
    if i >= len(mat) or j >= len(mat) or i < 0 or j < 0:
        return
    if mat[i][j] == 0 or visited[i][j] == 1:
        return
    if i == len(mat)-1 and j == len(mat)-1:
        ansList.append(s)
        return

    # agar return nhi ho rha call matlab yeh cell se hum travel karengye
    visited[i][j] = 1

    # making calls in all the four directions
    dfs(i-1,j,mat,s+'U',ansList,visited)
    dfs(i+1,j,mat,s+'D',ansList,visited)
    dfs(i,j-1,mat,s+'L',ansList,visited)
    dfs(i,j+1,mat,s+'R',ansList,visited)

    # after return is ecountered and hum piche backtrack kr rhe h toh unvisit krte jao
    # return aane ke baad call ke niche waali line execute hoti hai
    visited[i][j] = 0

def findPath(mat):

    s = ""
    ansList = []

    visited = []
    for x in range(len(mat)):
        list1 = []
        for y in range(len(mat)):
            list1.append(0)
        visited.append(list1)

    dfs(0, 0, mat, s, ansList, visited)
    return ansList


mat =   [[1,1,0],
         [1,1,1],
         [1,1,1]]

print(findPath(mat))