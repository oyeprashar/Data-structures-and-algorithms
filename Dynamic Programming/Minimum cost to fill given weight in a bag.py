INT_MAX = 3**38

class Solution:
    def findMinCost(self,currIndex,capacity,arr,memory):
        
        if capacity == 0: 
          return 0 
        
        if currIndex == len(arr):
          return INT_MAX
        
        if arr[currIndex] == -1 or capacity - (currIndex+1) < 0:
          return self.findMinCost(currIndex+1,capacity,arr,memory)
          
        if memory[currIndex][capacity] != -1:
            return memory[currIndex][capacity]
        
        op1 = arr[currIndex] + self.findMinCost(currIndex,capacity-(currIndex+1),arr,memory)
        op2 = self.findMinCost(currIndex+1,capacity,arr,memory)

        memory[currIndex][capacity] =  min(op1,op2)
        
        return memory[currIndex][capacity]
        
    def minimumCost(self, cost, n, W):
        
        memory = []
        for x in range(len(cost)):
            list1 = [] 
            for y in range(W+1):
                list1.append(-1)
            memory.append(list1)
        
        ans =  self.findMinCost(0,W,cost,memory)
        
        if ans == INT_MAX:
            return -1 
        else:
            return ans