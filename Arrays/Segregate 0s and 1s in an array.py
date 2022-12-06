
class Solution:
    
    def segregate(self, A, N): 
        
        left = 0
        right = len(A)-1
        
        while left < right:
            
            if A[left] == 0:
                left += 1
            
            if A[right] == 1:
                right -= 1
            
            if A[left] == 1 and A[right] == 0 and left < right:
                A[left],A[right] = A[right],A[left]
                left += 1
                right -= 1
            
        return A