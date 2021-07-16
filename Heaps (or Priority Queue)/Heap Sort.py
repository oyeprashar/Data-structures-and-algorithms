def heapify(currIndex,last,arr):

    newIndex = currIndex
    left = 2 * currIndex
    right = 2 * currIndex + 1

    if left <= last and arr[left] > arr[newIndex]:
        newIndex = left
    if right <= last and arr[right] > arr[newIndex]:
        newIndex = right

    if newIndex != currIndex:
        arr[newIndex],arr[currIndex] = arr[currIndex],arr[newIndex]
        heapify(newIndex,last,arr)

def convert2Heap(arr):
    lastNonLeafNode = len(arr) // 2
    last = len(arr)-1
    n = lastNonLeafNode

    while n != -1:
        heapify(n,last,arr)
        n -= 1

def heapSort(arr):
    convert2Heap(arr)
    last = len(arr)-1

    while last != -1:
        # swap the first and the last element
        arr[0],arr[last] = arr[last],arr[0]
        last -= 1
        heapify(0,last,arr)

    return arr
arr = [99,11,22,898,22,44]
print(heapSort(arr))