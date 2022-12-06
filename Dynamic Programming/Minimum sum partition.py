class Solution:
    
    def knapSack01(self,currIndex,currSet,totalSum,arr,memory):
        
        if currIndex == len(arr):
            return abs(currSet-(totalSum-currSet))

        if memory[currIndex][currSet] != -1:
            return memory[currIndex][currSet] 
        
        op1 = self.knapSack01(currIndex+1,currSet+arr[currIndex],totalSum,arr,memory)
        op2 = self.knapSack01(currIndex+1,currSet,totalSum,arr,memory)
        
        memory[currIndex][currSet]  = min(op1,op2)
        
        return memory[currIndex][currSet] 
    
    def minDifference(self, arr, n):
        
        totalSum = sum(arr)

        memory = []
        for x in range(len(arr)):
            list1 = []
            for y in range(totalSum+1):
                list1.append(-1)
            memory.append(list1)
        
        return self.knapSack01(0,0,totalSum,arr,memory)
