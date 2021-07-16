"""
Time complexity without the DP will be O(2^n1 * 2^n2) | Space complexity = O(n)
After DP the time complexity reduces to O(n1*n2) because we are filling a 2D matrix | Space complexity = O(n1*n2)
"""
def LCSHelper(i,j,string1,string2,memory):

    if i >= len(string1) or j >= len(string2):
        return 0

    if string1[i] == string2[j]:
        return 1 + LCSHelper(i+1,j+1,string1,string2,memory)

    op1 = LCSHelper(i+1,j,string1,string2,memory)
    op2 = LCSHelper(i,j+1,string1,string2,memory)

    memory[i][j] = max(op1,op2)

    return memory[i][j]


def LCS(string1,string2):

    # building the memory matrix
    memory = []
    for x in range(len(string1)):
        list1 = []
        for y in range(len(string2)):
            list1.append(-1)
        memory.append(list1)

    i = j = 0
    return LCSHelper(i,j,string1,string2,memory)

string1 = "ABCD"
string2 = "ABEDG"

print(LCS(string1,string2))