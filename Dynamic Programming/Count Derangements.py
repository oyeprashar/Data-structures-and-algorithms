# TIME COMPLEXITY : O(N) | SPACE COMPLEXITY : O(1)
class Solution:
    def disarrange(self, n):
      
        arr = [0,1]
        
        for i in range(3, n + 1):
            newValue = (i - 1) * (arr[1] + arr[0])
            arr[0] = arr[1]
            arr[1] = newValue
         
        return arr[1] 



# TIME COMPLEXITY : O(N) | SPACE COMPLEXITY : O(N)
class Solution:
    def disarrangeHelper(self,N,memory):
        
        if N == 0 or N == 1:
            return 0
        
        if N == 2:
            return 1
        
        if memory[N] != -1:
            return memory[N]
        
        memory[N] = (N-1)*(self.disarrangeHelper(N-1,memory) + self.disarrangeHelper(N-2,memory))
        return memory[N]
        
    def disarrange(self, N):
        
        memory = [-1] * (N+1)
        
        return self.disarrangeHelper(N,memory)