class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, mat, n):
        
        stack = []
        for i in range(len(mat)):
            stack.append(i)
        
        while len(stack) != 0 and len(stack) != 1:
            
            top1 = stack.pop()
            top2 = stack.pop()
            
            if mat[top1][top2] == 0 and mat[top2][top1] == 1:
                stack.append(top1)
            
            elif mat[top2][top1] == 0 and mat[top1][top2] == 1:
                stack.append(top2)
        
        if len(stack) == 0:
            return -1
        
        else:
            candidate = stack[0]
            
            for row in range(len(mat)):
                if row == candidate:
                    continue
                
                if mat[row][candidate] == 0:
                    return -1
                    
            for col in range(len(mat)):
                if col == candidate:
                    continue 
                
                if mat[candidate][col] == 1:
                    return -1
                    
            return candidate
                
            