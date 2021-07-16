"""
Input : arr[] = {4, 5, 6, 7, 6}
           k = 1
           x = 6
Output : 2
The first index of 6 is 2.

Input : arr[] = {20, 40, 50, 70, 70, 60}  
          k = 20
          x = 60
Output : 5
The index of 60 is 5
"""


def binarySearch(left,right,key,arr,ans):

    if left <= right:

        mid = (left+right) // 2

        if arr[mid] == key:
            # save and move to left to find its first occurence
            ans[0] = mid
            return binarySearch(left,mid-1,key,arr,ans)

        leftDiff = 3**38
        rightDiff = 3**38 

        if mid > 0:
            leftDiff = abs(key-arr[mid-1])
        if mid < len(arr)-1:
            rightDiff = abs(arr[mid+1]-key)

        if leftDiff < rightDiff:
            return binarySearch(left,mid-1,key,arr,ans)

        elif rightDiff <= leftDiff:
            return binarySearch(mid+1,right,key,arr,ans)

    else:
        return -1


def search(arr,key):
    ans = [-1]
    binarySearch(0,len(arr)-1,key,arr,ans)
    return ans[0]

arr1 = [4, 5, 6, 7, 6]
print(search(arr1,6))
arr2 = [20, 40, 50, 70, 70, 60]  
print(search(arr2,60))
arr3 = [5,8,10]
print(search(arr3,10))
array = [1, 2, 3, 1, 2, 7, 6, 4, 1]


