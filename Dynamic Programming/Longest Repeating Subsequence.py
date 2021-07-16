"""
Initialize memory with zeroes
"""
class Solution:
    def LongestRepeatingSubsequence(self, str):
        
        memory = []
        for x in range(len(str)+1):
            list1 = []
            for y in range(len(str)+1):
                list1.append(-1)
            memory.append(list1)
        
        
        for i in range(1,len(str)+1):
            for j in range(1,len(str)+1):
                
                if str[i-1] == str[j-1] and i != j:
                    memory[i][j] = memory[i-1][j-1] + 1
                
                else:
                    memory[i][j] = max(memory[i-1][j],memory[i][j-1])
        
        return memory[len(str)][len(str)]
                    
                    