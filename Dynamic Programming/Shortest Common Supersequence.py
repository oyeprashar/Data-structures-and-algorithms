class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        
        memory = []
        for x in range(len(str1)+1):
            list1 = []
            for y in range(len(str2)+1):
                list1.append(-1)
            memory.append(list1)
        
        for i in range(len(str1)+1):
            for j in range(len(str2)+1):
                
                if i == 0 or j == 0:
                    memory[i][j] = 0
                
                elif str1[i-1] == str2[j-1]:
                    memory[i][j] = memory[i-1][j-1] + 1
                
                elif str1[i-1] != str2[j-1]:
                    memory[i][j] = max(memory[i-1][j],memory[i][j-1])
                
        SCS = ""

        while i != 0 and j != 0:

            if str1[i-1] == str2[j-1]:
                SCS += str1[i-1]
                i -= 1
                j -= 1


            elif memory[i-1][j]> memory[i][j-1]:
                # before moving to the next row, we want to save the char corresponding to this row
                SCS += str1[i-1]
                i-= 1

            else:
                # before moving to another col we wat
                SCS += str2[j-1]
                j-= 1
            
        # jissme bhi abhi characters bache hai usse le lo
        while i > 0:
            SCS += str1[i-1]
            i -=1 
        
        while j > 0:
            SCS += str2[j-1]
            j -= 1
            

        SCS = SCS[::-1]

        return SCS


s = Solution()
str1 = "geek"
str2 = "eke"

print(s.shortestCommonSupersequence(str1,str2))