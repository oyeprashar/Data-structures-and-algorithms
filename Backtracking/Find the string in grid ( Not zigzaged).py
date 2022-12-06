#User function Template for python3

class Solution:
    def isPossible(self,i,j,grid,dir,currIndex,word,moveDict,visited):

        if currIndex == len(word):
            return True 
        
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return False 
        
        if visited[i][j] == True or grid[i][j] != word[currIndex]:
            return False
        
        if dir == None:
            for newDir in moveDict:
                move = moveDict[newDir]
    
                curri = i + move[0]
                currj = j + move[1]
    
                visited[i][j] = True
                if self.isPossible(curri,currj,grid,newDir,currIndex+1,word,moveDict,visited) == True:
                    visited[i][j] = False
                    return True 
                visited[i][j] = False
            
        else:
            move = moveDict[dir]
            curri = i + move[0]
            currj = j + move[1]
    
            visited[i][j] = True
            if self.isPossible(curri,currj,grid,dir,currIndex+1,word,moveDict,visited) == True:
                visited[i][j] = False
                return True 
            visited[i][j] = False
        
    
        
        
    def searchWord(self, grid, word):
        
        visited = []
        for x in range(len(grid)):
            list1 = []
            for y in range(len(grid[0])):
                list1.append(False)
            visited.append(list1)

        moveDict = { "up":[-1,0], "down":[1,0], "left":[0,-1], "right":[0,1], "upleft":[-1,-1], "upright":[-1,1], "downleft":[1,-1], "downright":[1,1]}

        ans = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == word[0]:

                    if self.isPossible(i,j,grid,None,0,word,moveDict,visited) == True:
                        ans.append((i,j))

        return ans