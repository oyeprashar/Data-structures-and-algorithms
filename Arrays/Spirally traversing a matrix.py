class Solution:
    
    #Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self,matrix, r, c): 
        
        top = 0
        right = c - 1
        left = 0 
        down = r - 1
        dir = 0
        ans = []
        
        while top <= down and left <= right:
            
            if dir == 1:
                # row = top,
                # col = left --> right
                for col in range(left,right+1):
                    ans.append(matrix[top][col])
                top += 1
            
            if dir == 1:
                # row = top--> down
                # col = right
                for row in range(top,down+1):
                    ans.append(matrix[row][right])
                right -= 1
            
            if dir == 2:
                # row = down
                # col if decrements from right to left
                for col in range(right,left-1,-1):
                    ans.append(matrix[down][col])
                down -= 1
            
            if dir == 3:
                # row = down -- > top
                # col = left
                for row in range(down,top-1,-1):
                    ans.append(matrix[row][left])
                left += 1
            
            dir = (dir+1)%4
            
        return ans          