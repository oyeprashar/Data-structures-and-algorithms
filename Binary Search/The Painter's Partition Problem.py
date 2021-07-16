
class Solution:
    
    def isValid(self,currTime,pAvail,boards):
        pNeeded = 1
        painted = 0
        
        for board in boards: 
            if board > currTime:
                return False
            if painted + board > currTime:
                pNeeded += 1
                painted = board
            else:
                painted += board
            
        return pNeeded <= pAvail
        
    def binarySearch(self,left,right,pAvail,boards,ans):
        
        if left <= right:
            
            mid = (left+right) // 2
            
            if self.isValid(mid,pAvail,boards) == True:
                ans[0] = mid
                return self.binarySearch(left,mid-1,pAvail,boards,ans)
            else:
                return self.binarySearch(mid+1,right,pAvail,boards,ans)
        
    def minTime (self, arr, n, k):
        ans = [-1]
        left = 0
        right = sum(arr)
        self.binarySearch(left,right,k,arr,ans)
        return ans[0]