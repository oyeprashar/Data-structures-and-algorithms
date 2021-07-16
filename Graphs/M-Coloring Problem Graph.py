
def completed(arr):
    for x in arr:
        if x == -1:
            return False
    return True

def coloring(currV,V,k,mat,colored,ans):

    if completed(colored) == True:
        ans[0] = True
        return True

    if currV == V:
        return 

    for color in range(1,k+1):
        possible = True

        for nbr in range(V):
            if mat[currV][nbr] == 1 and colored[nbr] == color:
                possible = False

        if possible == True:
            colored[currV] = color
            if coloring(currV+1,V,k,mat,colored,ans) == True: # agar koi recursive call gets True, we will not search any more and return True
                return True
            colored[currV] = -1

def graphColoring(graph, k, V):
    
    colored = [-1] * (V)
    ans = [False]
    currV = 0
    coloring(currV,V,k,graph,colored,ans)
    return ans[0]

V = 4
k = 1
graph = [[0, 1, 1, 1],
       [1, 0, 1, 0],
       [1, 1, 0, 1],
       [1, 0, 1, 0]]

print(graphColoring(graph,V,k))