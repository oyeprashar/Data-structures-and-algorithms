def LCS(str1,str2):

    memory = []
    for x in range(len(str1)+1):
        list1 = []
        for y in range(len(str2)+1):
            list1.append(-1)
        memory.append(list1)
    
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):

            if str1[i-1] == str2[j-1]:
                memory[i][j] = 1 + memory[i-1][j-1]
            
            else:
                memory[i][j] = max(memory[i-1][j],memory[i][j-1])
            
    ans = ""
    while i != 0 and j != 0:

        if str1[i-1] == str2[j-1]:
            ans += str1[i-1]
            i -= 1
            j -= 1
        
        else:
            if memory[i-1][j] > memory[i][j-1]:
                i -= 1
            else:
                j -= 1
            
    return ans[::-1]

X = "AGGTAB"
Y = "GXTXAYB"
print(LCS(X,Y))




