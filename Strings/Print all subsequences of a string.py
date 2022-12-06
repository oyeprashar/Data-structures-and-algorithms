"""
Print all subsequences of a string

Input : abc
Output : a, b, c, ab, bc, ac, abc

Input : aaa
Output : a, a, a, aa, aa, aa, aaa
"""

def printSubsequence(str1, currIndex, currSequence):

    if currIndex >= len(str1):
        print(currSequence)
        return 

    # To generate the subsequence of a string, at each character I have two options
    #   1. include it in the current sequence
    #   2. Don't include it in the current sequence

    currSequence.append(str1[currIndex])
    printSubsequence(str1, currIndex + 1, currSequence)
    currSequence.pop()
    printSubsequence(str1, currIndex + 1, currSequence)


str1 = 'abc'
printSubsequence(str1, 0, [])