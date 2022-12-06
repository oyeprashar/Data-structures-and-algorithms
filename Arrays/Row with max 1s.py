class Solution:

	def rowWithMax1s(self,grid, n, m):
	    
		minCol = 3**38
        row = -1
        ans = -1
        colRange = m
        
        # print(grid)
    
        for i in range(n):
            for j in range(colRange):
                
                if grid[i][j] == 1:
                    if j < minCol:
                        minCol = j
                        ans = i
                        colRange = j
                        break
                        # we break and change the variable for the next loop
                    
            if colRange-1 < 0:
                break
    
        return ans
