class Solution:
    def maxProduct(self, arr):
        maxP = arr[0]
        minP = arr[0]
        ans = arr[0]
        
        for i in range(1,len(arr)):
            
            if arr[i] < 0:
                maxP,minP = minP,maxP
                
            maxP = max(arr[i],arr[i]*maxP)
            minP = min(arr[i],arr[i]*minP)
            
            ans = max(ans,maxP)
        
        return ans