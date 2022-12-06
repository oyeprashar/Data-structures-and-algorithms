# we have to do this like LIS
class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        
        arr = []
        maxProfit = -3**38
        for i in range(len(startTime)):
            arr.append([startTime[i],endTime[i],profit[i]])
            maxProfit = max(maxProfit,profit[i])
                
        arr.sort(key = lambda item : item[1])

        memory = []
        

        for item in arr:
            memory.append(item[2])

        for i in range(1,len(memory)):
            for j in range(i):

                # if both are non overlapping
                if arr[i][0] >= arr[j][1]:
                    memory[i] = max(memory[i],arr[i][2]+memory[j])
                    maxProfit = max(maxProfit,memory[i])

        return maxProfit