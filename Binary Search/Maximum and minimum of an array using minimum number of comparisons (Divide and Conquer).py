"""
Finding min and max using divde and conquer method which is efficient 
before very less number of comparison are needed

Time complexity = O(logn)
"""

def find(arr):

    if len(arr) == 1:
        return arr[0],arr[0]

    if len(arr) == 2:
        if arr[0] > arr[1]:
            currMax = arr[0]
            currMin = arr[1]
        else:
            currMax = arr[1]
            currMin = arr[0]
        return currMax,currMin


    mid = len(arr) // 2

    left = arr[:mid]
    right = arr[mid:]

    max1,min1 = find(left)
    max2,min2 = find(right)

    if max1 > max2:
        maxAns = max1
    else:
        maxAns = max2
    if min1 < min2:
        minAns = min1
    else:
        minAns = min2
    return maxAns,minAns

arr1 = [1000, 11, 445, 1, 330, 3000]
arr2 = [5,7,3,4,9,12,6,2] 
print(find(arr1))
print(find(arr2))