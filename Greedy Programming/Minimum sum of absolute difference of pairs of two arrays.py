"""
Minimum sum of absolute difference of pairs of two arrays

Algorithm:
Bascially we want to substract the max of arr1 with available max from arr2 to minimize the diffrence, so subtracting the elements at same index is basically doing 
the same thing. 
"""

def findMinDiff(arr1,arr2):

    arr1.sort()
    arr2.sort()

    ans = 0

    for i in range(len(arr1)):

        ans += abs(arr1[i]-arr2[i])
    
    return ans

arr1 = [4, 1, 8, 7]
arr2 = [2, 3, 6, 5]

print(findMinDiff(arr1,arr2))

