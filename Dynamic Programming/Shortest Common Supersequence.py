def shortestCommonSupersequence(str1,str2):

    # first we need to find the LCS and build the memory
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

    lenOfLCS = memory[len(str1)][len(str2)]

    return abs((len(str1)+len(str2))-lenOfLCS)


    # <- If you want to see the supersequence then execute this code

#     LCS = "" 

#     # finding the actual LCS from the memory
#     while i > 0 and j > 0:

#         if str1[i-1] == str2[j-1]:
#             LCS += str1[i-1]
#             i -= 1
#             j -= 1

#         else:
#             if memory[i-1][j] > memory[i][j-1]:
#                 i -= 1
#             else:
#                 j -= 1

#     LCS = LCS[::-1]

#     ans = ""

#     for char in str1:
#         if char not in LCS:
#             ans += char
#     for char in str2:
#         if char not in LCS:
#             ans += char

#     ans += LCS
#     return ans

str1 = "efgh"; str2 = "jghi"
print(shortestCommonSupersequence(str1,str2))
