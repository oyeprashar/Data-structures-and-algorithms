class Solution:
    def maxGold(self, n, m, grid):
        
        memory = []
        for x in range(n):
            list1 = []
            for y in range(m):  
                list1.append(0)
            memory.append(list1)
        
        # we need to fill the first col as it is
        maxCollected = 0
        
        for row in range(n):
            memory[row][0] = grid[row][0]
            maxCollected = max(maxCollected,grid[row][0])
        
        # now we need to fill each col 
        moves = [(-1,-1),(0,-1),(1,-1)]

    
        for col in range(1,m):
            for row in range(n):

                maxValue = 0
                for move in moves:
                    if row + move[0] >= 0 and row + move[0] < n and col + move[1] >= 0 and col + move[1] < m:
                        currRow = row + move[0]
                        currCol = col + move[1]
                        maxValue = max(maxValue,memory[currRow][currCol] + grid[row][col])

                memory[row][col] = maxValue 

                if col == m-1:
                    maxCollected = max(maxCollected,memory[row][col])
                    
    
        return maxCollected