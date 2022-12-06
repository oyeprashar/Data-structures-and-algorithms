class Solution:
    
    def findWinner(self,char,board):
        
        # checking the rows
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == char:
                return True
        
        # checking the col
        for j in range(len(board)):
            if board[0][j] == board[1][j] == board[2][j] == char:
                return True
        
        # checking the principal diagonal
        if board[0][0] == board[1][1] == board[2][2] == char:
            return True
    
        if board[0][2] == board[1][1] == board[2][0] == char:
            return True
        
        return False
    
    def validTicTacToe(self, board: List[str]) -> bool:
        
        
        countX = 0
        countO = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    countX += 1
                
                elif board[i][j] == 'O':
                    countO += 1
        
        
        if abs(countO - countX) > 1 or countO > countX:
            return False
        
        isXWinner = self.findWinner('X',board)
        isOWinner = self.findWinner('O',board)
        
        if isXWinner == True and isOWinner == True:
            return False
        
        if isXWinner == True and abs(countX-countO) != 1:
            return False
        
        if isOWinner == True and abs(countX-countO) != 0:
            return False
        