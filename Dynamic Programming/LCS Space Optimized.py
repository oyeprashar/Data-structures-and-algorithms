class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,str1,str2):
        
        memory = []
        for x in range(2):
            list1 = []
            for y in range(len(str2)+1):
                list1.append(0)
            memory.append(list1)
    
        maxLen = 0
            
        for i in range(1,len(str1)+1):
            for j in range(1,len(str2)+1):
    
                if str1[i-1] == str2[j-1]:
                    memory[1][j] = 1 + memory[0][j-1]
                    maxLen = max(maxLen,memory[1][j])
                
                else:
                    memory[1][j] =  max(memory[1][j-1], memory[0][j])
                
            for col in range(len(str2)):
                memory[0][col] = memory[1][col]
                memory[1][col] = 0 
    
        return maxLen