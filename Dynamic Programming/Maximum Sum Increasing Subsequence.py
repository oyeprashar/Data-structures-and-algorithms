class Solution:
    def maxSumIS(self, arr, n):
        
        memory = arr.copy()
        maxValue = arr[0]

        for i in range(1,len(arr)):
            for j in range(i):
                
                if arr[j] < arr[i]:
                    memory[i] = max(memory[i],arr[i] + memory[j])
                    maxValue = max(maxValue,memory[i])

        return maxValue
        