"""
BINARY SEARCH
"""

def binarySearchHelper(l,r,arr,key):

    if l <= r:
        mid = (l + r) // 2

        if arr[mid] == key:
            return mid

        elif key < arr[mid]:
            return binarySearchHelper(l,mid-1,arr,key)

        else:
            
            return binarySearchHelper(mid+1,r,arr,key)

    else:
        return -1

def binarySearch(arr,key):
    l = 0
    r = len(arr) - 1

    return binarySearchHelper(l,r,arr,key)

arr = [1,2,3,4,100,102,199,200,299]
print(binarySearch(arr,298))