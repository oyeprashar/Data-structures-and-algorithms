class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        
        maxElement = arr[-1]
        minElement = arr[0]
        ans = maxElement - minElement
        
        for i in range(1,len(arr)):
            
            if min(arr[i]-k,arr[0]+k) < 0:
                continue
            
            maxElement = max(arr[i-1]+k,arr[-1]-k)
            minElement = min(arr[i]-k,arr[0]+k)
            
            
            
            ans = min(ans,maxElement-minElement)
        
        return ans
        