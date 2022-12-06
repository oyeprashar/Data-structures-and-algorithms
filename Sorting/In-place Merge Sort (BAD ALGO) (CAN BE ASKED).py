# arr = [9,8,3,7,5,6,4,1]

def shellSort(left,right,arr1):
    n = (right-left) + 1
    gap = n // 2

    while gap > 0:

        j = left + gap
        i = left

        while j <= right:
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            i += 1
            j += 1

        x = (i-gap) + 1

        while x >= left:
            if arr[x] > arr[i]:
                arr[x],arr[i] = arr[i],arr[x]
            x -= 1
            i -= 1
        gap //= 2


def mergeSort(left,right,arr):

    if left == right:
        return 

    mid = (left+right) // 2

    mergeSort(left,mid,arr)
    mergeSort(mid+1,right,arr)

    shellSort(left,right,arr)

arr = [9,8,3,7,5,6,4,1]
mergeSort(0,len(arr)-1,arr)
print(arr)
