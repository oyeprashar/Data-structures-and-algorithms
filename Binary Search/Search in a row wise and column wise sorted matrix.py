"""
mat = [[10, 20, 30, 40],
	   [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]
"""

# iterative approach to search the sorted 2d matrix (efficient and got accepted at GFG)
class Solution:

	def matSearch(self,mat, N, M, key):
	    i = 0;
	    j = len(mat[0])-1
	    
	    while i < len(mat) and j >= 0:
	    
	        if mat[i][j] == key:
	            return 1
	    
	        if key > mat[i][j]:
	            i += 1
	    
	        else:
	            j -= 1
	    return 0

# recursive approach (got accepted at Leetcode but not on GFG)
class Solution:
    def binarySearch(self,i,j,key,mat):
        
        if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]):
            return 0
        
        if mat[i][j] == key:
            return 1
            
        if key > mat[i][j]:
            return self.binarySearch(i+1,j,key,mat)
        else:
            return self.binarySearch(i,j-1,key,mat)
        
    def searchMatrix(self, matrix, target):
        return self.binarySearch(0,len(matrix[0])-1,target,matrix)



 
