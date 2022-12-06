"""
Input: N = 3, K = 4 
Output: 231 
Explanation: 
The ordered list of permutation sequence from integer 1 to 3 is : 123, 132, 213, 231, 312, 321. So, the 4th permutation sequence is “231”.
"""

def permutate(l,arr,ans):
    if l == len(arr)-1: # we are at last index it means that no more elements are there to form combinations with and all combinations are already formed
        num = int("".join(arr))
        ans.append(num)
        return

    for i in range(l,len(arr)):
        arr[l],arr[i] = arr[i],arr[l]
        permutate(l+1,arr,ans)
        arr[l],arr[i] = arr[i],arr[l]

def getKthPermutations(N,k):
    string = ""
    for x in range(1,N+1):
        string += str(x)

    arr = [char for char in string]
    l = 0
    ans = []
    permutate(l,arr,ans)
    return ans[k-1]


print(getKthPermutations(3,3))
print(getKthPermutations(2,1))

