class Solution:
    def findOneCount(self,i,j,board):
        
        dr = [-1, 1, 0, 0, -1, -1, 1 ,1]
        dc = [ 0, 0,-1, 1, -1,  1,-1, 1 ]
        count = 0
        
        for x in range(len(dr)):
            
            p = i +  dr[x]
            q = j + dc[x]
            
            if p >= 0 and q >= 0 and p < len(board) and q < len(board[0]):
                if board[p][q] == 1 or board[p][q] == 2:
                    count += 1
            
        return count
        
        
    def gameOfLife(self, board: List[List[int]]) -> None:
       

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                count = self.findOneCount(i,j,board)
                
                if board[i][j] == 1 and count >= 0 and count <= 1:
                    board[i][j] = 2
                
                elif board[i][j] == 1 and count >= 2 and count <= 3:
                    board[i][j] = 1
                
                elif board[i][j] == 1 and count >= 3 and count <= 8:
                    board[i][j] = 2
                    
                elif board[i][j] == 0 and count == 3:
                    board[i][j] = 3
                

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 0
                    
                elif board[i][j] == 3:
                    board[i][j] = 1
                
                