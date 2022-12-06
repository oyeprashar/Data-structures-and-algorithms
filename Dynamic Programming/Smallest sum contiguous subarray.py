"""
Input : arr[] = {3, -4, 2, -3, -1, 7, -5}
Output : -6
Subarray is {-4, 2, -3, -1} = -6

Input : arr = {2, 6, 8, 1, 4}
Output : 1
"""

def smallestContigousSum(arr):

    currSum = arr[0]
    minSum = arr[0]

    for i in range(1,len(arr)):

        if arr[i] < currSum + arr[i]:
            currSum = arr[i]
        
        else:
            currSum += arr[i]
        

        minSum = min(minSum,currSum)
    
    return minSum

arr1 = [3, -4, 2, -3, -1, 7, -5]
arr2 = [2, 6, 8, 1, 4]
print(smallestContigousSum(arr1))
print(smallestContigousSum(arr2))
        

