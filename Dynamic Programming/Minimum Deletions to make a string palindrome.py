"""
Minimum Deletions to make a string palindrome
=== LOGIC ==
-> We need to find how many chars are different from its reverse, if we remove them that the string will become a palindrome
-> So we find the number of chars that are common between the string and its reverse and return the abs(len(string)-lenOfLCS) 
-> this will represent the number of chars that needs to be deleted to make the string a palindrome
"""
class Solution:
    def minimumNumberOfDeletions(self,S):
        str1 = S
        str2 = S[::-1]
        
        # finding the LCS of input string with its reverse
        
        memory = []
        for x in range(len(str1)+1):
            list1 = []
            for y in range(len(str2)+1):
                list1.append(-1)
            memory.append(list1)
            
        for i in range(len(str1)+1):
            for j in range(len(str2)+1):
                
                if i == 0 or j == 0:
                    # dono me se koi bhi string agar empty
                    # dono me se koi bhi string agar empty
                    memory[i][j] = 0
                
                elif str1[i-1] == str2[j-1]:
                    memory[i][j] = memory[i-1][j-1] + 1
                
                elif str1[i-1] != str2[j-1]:
                    memory[i][j] = max(memory[i-1][j],memory[i][j-1])
                
        lenOfLCS = memory[len(str1)][len(str2)]
        
        return abs(len(str1)-lenOfLCS)