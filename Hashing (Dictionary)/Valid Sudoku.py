class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = [set() for _ in range(9)]
        col =  [set() for _ in range(9)]
        box =  [set() for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                
                if board[i][j] == ".":
                    continue
                
                currElement = board[i][j]
                
                if currElement in row[i]:
                    return False
                else:
                    row[i].add(currElement)
                
                if currElement in col[j]:
                    return False
                else:
                    col[j].add(currElement)
                
                boxIndex = (i//3)*3 + (j//3)
                
                if currElement in box[boxIndex]:
                    return False
                else:
                    box[boxIndex].add(currElement)
            
        return True