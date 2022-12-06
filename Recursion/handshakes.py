class Solution:
    def handShakes(self,currIndex,arr,totalN,ans):

        if currIndex == len(arr):
            ans[0] += 1
            return 
        
        if arr[currIndex] != -1:
            return self.handShakes(currIndex+1,arr,totalN,ans)
        

        for i in range(currIndex+1,len(arr)):
            if arr[i] == -1:
                arr[currIndex] = i
                arr[i] = currIndex
                self.handShakes(currIndex+1,arr,totalN,ans)
                arr[currIndex] = -1 
                arr[i] = -1
    
            else:
                return 
    
    def count(self, N):
        ans = [0]
        arr = [-1] * N
        self.handShakes(0,arr,N,ans)
        return ans[0]
