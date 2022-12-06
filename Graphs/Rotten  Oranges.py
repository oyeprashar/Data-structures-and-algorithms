from collections import deque

class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		
		queue = deque([])
        fresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 2:
                    queue.append([i,j])
                
                if grid[i][j] == 1:
                    fresh += 1
                    
        if fresh == 0:
            return 0
        
        dr = [-1,1,0,0]
        dc = [0,0,-1,1]
                
        timeTaken = 0
        totalRotten = 0
        
        while len(queue) > 0:
            
            size = len(queue)
            
            for _ in range(size):
            
                curr = queue.popleft()
                curri = curr[0]
                currj = curr[1]

                for x in range(4):
                    nbri = curri + dr[x]
                    nbrj = currj + dc[x]

                    if nbri >= 0 and nbrj >= 0 and nbri < len(grid) and nbrj < len(grid[0]):
                        if grid[nbri][nbrj] == 1:

                            queue.append([nbri,nbrj])
                            grid[nbri][nbrj] = 2
            
            if len(queue) > 0:
                totalRotten += len(queue)
                timeTaken += 1
        
        if fresh > totalRotten:
            return -1
        return timeTaken