class Solution:
    def getMinDiff(self, arr, n, k):
        
        arr.sort()
        
        maxElement = arr[-1]
        minElement = arr[0]
        ans = maxElement - minElement
        
        # the smaller is increased by k
        # the bigger is decreased by k
        
        for i in range(1,len(arr)):
            
            maxElement = max(arr[i-1]+k,arr[-1]-k)
            minElement = min(arr[i]-k,arr[0]+k)
            
            ans =  min(ans,maxElement - minElement)
        
        return ans