class Solution:
    
    def isPossible(self,i,j,currIndex,word,grid,moves,visited):
        
        if currIndex == len(word):
            return True


        if visited[i][j] == True or grid[i][j] != word[currIndex]:
            return False 
            
        for move in moves:
            
            curri = i + move[0]
            currj = j + move[1]
            

            if curri >= 0 and currj >= 0 and curri < len(grid) and currj < len(grid[0]):
            
                visited[i][j] = True
                if self.isPossible(curri,currj,currIndex+1,word,grid,moves,visited) == True:
                    return True
                visited[i][j] = False
        
        return False
        
            
    def searchWord(self, grid, word):

        visited = []
        for x in range(len(grid)):
            list1 = []
            for y in range(len(grid[0])):
                list1.append(False)
            visited.append(list1)
            
        moves = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == word[0]:
                    if self.isPossible(i,j,0,word,grid,moves,visited) == True:
                        count += 1
                    
        return count

s = Solution()
 
str1 = "MAGIC"
grid = ["BBABBM","CBMBBA","IBABBG",
            "GOZBBI","ABBBBC","MCIGAM"]


 
print(s.searchWord(grid,str1))