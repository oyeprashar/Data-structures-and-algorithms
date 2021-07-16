"""
generate all the permutation of the input string
it means all the characters in the strings should be swapped with all the other characters and with iteself too!
current se swap ka matlab h wahi same string ek permutation bhi h
"""

def permutate(l,r,strArr,ans):

    if l == r: # if l is at the last index it means that all permutations are already generated and no more elements are ahead.
        curr = "".join(strArr)
        ans.append(curr)
        return

    for i in range(l,r+1):
        # swap elements at i and r
        strArr[l],strArr[i] = strArr[i],strArr[l]
        permutate(l+1,r,strArr,ans)
        # unswap for other permutations
        strArr[l],strArr[i] = strArr[i],strArr[l]

def getPermutations(string):
    strArr = list(string)
    l = 0
    r = len(string)-1
    ans = []

    permutate(l,r,strArr,ans)
    return ans

string = "ABC"
print(getPermutations(string))

