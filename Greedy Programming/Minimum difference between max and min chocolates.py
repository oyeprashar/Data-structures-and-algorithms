"""
N = 8, M = 5
A = {3, 4, 1, 9, 56, 7, 9, 12}
Output: 6
Explanation: The minimum difference between 
maximum chocolates and minimum chocolates 
is 9 - 3 = 6 by choosing following M packets :
{3, 4, 9, 7, 9}.
"""
def findMinDiff(A,N,M):
    
    A.sort()
    
    i = 0
    j = i + M - 1
    minDiff = A[j] - A[i]
    
    print(A)
    
    while j < len(A):
        
        currDiff = A[j] - A[i]
        print("start =",i,A[i],"end =",j,A[j],"diff =",currDiff)
        minDiff = min(minDiff,currDiff)
        i += 1
        j += 1
    
    return minDiff

N = 8
M = 5
A = [3, 4, 1, 9, 56, 7, 9, 12]

print(findMinDiff(A,N,M))