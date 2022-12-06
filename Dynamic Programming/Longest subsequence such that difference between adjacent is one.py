class Solution:
    def longestSubsequence(self, N, A):
        
        memory = [1] * N 
        maxLen = 1
        
        for i in range(1,N):
            for j in range(i):
                
                if abs(A[i] - A[j]) == 1:
                    memory[i] = max(memory[i],memory[j]+1)
                    maxLen = max(maxLen,memory[i])
        
        return maxLen