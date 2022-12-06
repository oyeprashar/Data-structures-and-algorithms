class Solution:
    def search(self,i,j,grid,currIndex,word,visited,moves):
        
        if currIndex == len(word):
            return True
        
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 
        
        if visited[i][j] == True or grid[i][j] != word[currIndex]:
            return False
        

        visited[i][j] = True
        
        for move in moves:
            curri = i + move[0]
            currj = j + move[1]
            
            if self.search(curri,currj,grid,currIndex+1,word,visited,moves) == True:
                return True
            
        visited[i][j] = False
        
               
    def exist(self, grid: List[List[str]], word: str) -> bool:
        
        if len(grid) == 1 and len(grid[0]) ==1:
            # print("yes")
            if grid[0][0] == word:
                return True
            else:
                return False
            
        moves = [(-1,0),(1,0),(0,-1),(0,1)] #(-1,-1),(-1,1),(1,-1),(1,1)]

            
        res = []

        visited = []
        for x in range(len(grid)):
            list1 = []
            for y in range(len(grid[0])):
                list1.append(False)
            visited.append(list1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == word[0]:
                    if self.search(i,j,grid,0,word,visited,moves) == True:
                        return True

        return False