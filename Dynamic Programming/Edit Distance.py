class Solution:
    def minDistHelper(self,i,j,str1,str2,memory):
        
        if i < 0 and j < 0:
            return 0 
        
        if i < 0:
            return j + 1
        
        if j < 0:
            return i + 1
        
        if memory[i][j] != -1:
            return memory[i][j]

        if str1[i] == str2[j]:
            return self.minDistHelper(i-1,j-1,str1,str2,memory)


        # replace 
        op1 = 1 + self.minDistHelper(i-1,j-1,str1,str2,memory)

        # insert 
        op2 = 1 + self.minDistHelper(i,j-1,str1,str2,memory)

        # remove or delelte
        op3 = 1 + self.minDistHelper(i-1,j,str1,str2,memory)

        memory[i][j] = min(op1,op2,op3)
        
        return memory[i][j]
        
    def minDistance(self, word1: str, word2: str) -> int:
        memory = []
        for x in range(len(word1)):
            list1 = []
            for y in range(len(word2)):
                list1.append(-1)
            memory.append(list1)
            
        
        return self.minDistHelper(len(word1)-1,len(word2)-1,word1,word2,memory)
        