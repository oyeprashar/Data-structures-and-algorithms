"""
Bottom up Longest common subsquence 
 Driver program
X = "AGGTAB"
Y = "GXTXAYB"

Output:
GTAB | 4
"""

def LCS(str1,str2):

    memory = []
    for x in range(len(str1)+1):
        list1 = []
        for y in range(len(str2)+1):
            list1.append(-1)
        memory.append(list1)

    ans = -3**38
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):

            if i == 0 or j == 0:
                memory[i][j] = 0

            elif str1[i-1] == str2[j-1]:
                memory[i][j] = memory[i-1][j-1] + 1
                

            elif str1[i-1] != str2[j-1]:
                memory[i][j] = max(memory[i-1][j],memory[i][j-1])

            ans = max(ans,memory[i][j])

    # ==== printing the LCS ====
    output = ""
    i = len(str1)
    j = len(str2)

    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            output += str1[i-1]
            i -= 1
            j -= 1

        else:
            if memory[i-1][j] > memory[i][j-1]:
                i -= 1
            else:
                j-= 1

    return output[::-1]
 



    return ans
X = "AGGTAB"
Y = "GXTXAYB"
print(LCS(X,Y))
