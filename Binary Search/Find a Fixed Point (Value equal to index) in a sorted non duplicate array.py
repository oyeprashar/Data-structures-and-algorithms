"""
-> Find an element whose value is equal to its index
-> The input array is sorted
-> No duplicate elements

If the input array is sorted then this can be done in O(logn) time using binary search
"""

def binarySearch(left,right,arr):

    if left <= right:

        mid = (left+right) // 2

        if mid == arr[mid]:
            return mid

        if arr[mid] > mid:
            # this means isske aage waale element toh isse bhi bade hongye aur woh bhi aapne indices se bade hongye
            return binarySearch(left,mid-1,arr)
        else:
            return binarySearch(mid+1,right,arr)
    else:
        return -1

def getFixedPoint(arr):

    return binarySearch(0,len(arr)-1,arr)

arr = [-10, -1, 0, 3, 10, 11, 30, 50, 100]
arr = [-10, -1, 0, 2, 4]
print(getFixedPoint(arr))
