"""
Longest Palindromic Subsequence
==== LOGIC ====
Find the longest common subsequence between the input string and the reverse of it and we will find the Longest Palindromic Subsequence
"""

def longestPalindromic(str1):

    str2 = str1[::-1]

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
                # incrementing the count that we were keeping
                memory[i][j] = memory[i-1][j-1] + 1

            elif str1[i-1] != str2[j-1]:
                # agar match nhi hua toh try combinations
                # trying all the possible comibinations
                memory[i][j] = max(memory[i-1][j],memory[i][j-1])


    return memory[i][j]



    # for list2 in memory:
    #     print(list2)

# str1 = "GEEKSFORGEEKS"
str1 = "bbbab"
print(longestPalindromic(str1))
