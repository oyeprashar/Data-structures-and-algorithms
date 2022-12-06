class Solution:
    
    def findLongestConseqSubseq(self,arr, N):
        
        maxElement = max(arr)
        freq = [0] * (maxElement+1)
        
        for num in arr:
            freq[num] += 1
        
        currCount = 0
        maxCount = 0
        
        for i in range(len(freq)):
            
            if freq[i] == 1:
                currCount += 1
            
            else:
                currCount = 0
            
            maxCount = max(maxCount,currCount)
        
        return maxCount