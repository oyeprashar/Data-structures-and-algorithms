class Solution:
    
    def equilibriumPoint(self,arr, N):
        
        if len(arr) == 1:
            return 1
        
        totalSum = sum(arr)
        leftSum = 0 
        
        for i in range(len(arr)):
            
            rightSum = totalSum - (leftSum + arr[i])
            
            if leftSum == rightSum:
                return i + 1
            
            leftSum += arr[i]
            
        return -1