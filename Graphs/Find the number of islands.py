class Solution:
    #all 8 directions.    
    def DFS(self,i,j,grid,visited):
        
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return 
    
        if grid[i][j] == "0" or visited[i][j] == True:
            return 
    
        visited[i][j] = True
        self.DFS(i-1,j,grid,visited)    # up
        self.DFS(i+1,j,grid,visited)    # down   
        self.DFS(i,j-1,grid,visited)    # left
        self.DFS(i,j+1,grid,visited)    # right
        self.DFS(i-1,j-1,grid,visited)    # dia upper left
        self.DFS(i-1,j+1,grid,visited)    # dia upper right
        self.DFS(i+1,j-1,grid,visited)    # dia lower left
        self.DFS(i+1,j+1,grid,visited)    # dia lower right
        
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = []

        for x in range(len(grid)):
            list1 = []
            for y in range(len(grid[0])):
                list1.append(False)
            visited.append(list1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1" and visited[i][j] == False:

                    count += 1
                    self.DFS(i,j,grid,visited)
        return count