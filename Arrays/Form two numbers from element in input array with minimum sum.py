"""
Input:
N = 6
Arr[] = {6, 8, 4, 5, 2, 3}
Output: 604
Explanation: The minimum sum is formed 
by numbers 358 and 246.
"""

def getRes(arr):

    arr.sort()
    str1 = ""
    str2 = ""

    for i in range(len(arr)):

        if i % 2 == 0:
            str1 += str(arr[i])
        else:
            str2 += str(arr[i])

    return int(str1) + int(str2)

arr1 = [6,8,4,5,2,3]
arr2 = [5, 3, 0, 7, 4]
arr3 = [1,3,8,7,4,2,7,7,9,3,1,9,8,6,5,0,2,8,6,0,2,4]
print(getRes(arr1))
print(getRes(arr2))
print(getRes(arr3))