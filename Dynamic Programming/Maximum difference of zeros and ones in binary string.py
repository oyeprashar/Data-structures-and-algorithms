INT_MIN = -3**38

class Solution:
    
    def maxSubstring(self, S):
        
        if S == "1"*len(S):
            return -1 
        
        curr = 0
        maxDiff = INT_MIN 
        
        for i in range(len(S)):
            
            if S[i] == "0":
                num = 1
            else:
                num = -1
            
            if num > curr + num:
                curr = num
            
            else:
                curr += num 
            
            maxDiff = max(maxDiff,curr)
        
        return maxDiff
