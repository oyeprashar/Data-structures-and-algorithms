class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
        memory = []
        for p in range(x+1):
            list1 = []
            for q in range(y+1):
                list1.append(0)
            memory.append(list1)
    
        for i in range(1,x+1):
            for j in range(1,y+1):
                
                if s1[i-1] == s2[j-1]:
                    memory[i][j] = 1 + memory[i-1][j-1]
                
                elif s1[i-1] != s2[j-1]:
                    memory[i][j] = max(memory[i-1][j],memory[i][j-1])
                
                
        return memory[x][y]
        
print(LCS(X,Y))
