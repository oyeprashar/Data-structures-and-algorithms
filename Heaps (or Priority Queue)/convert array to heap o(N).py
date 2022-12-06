"""
ALGORITHM TO CONVERT ARRAY INTO HEAP IN O(N) TIME
    -> find the last non leaf node using len(inputArray) // 2
    -> from this last non leaf node heapify till the index 1
Note: hepify checks the parent with its children
"""


class Heap:
    def __init__(self, type1=False):
        self.type1 = type1

    def compareHeapify(self, chidIndex, newIndex, array):
        if self.type1 is False:
            return array[chidIndex] < array[newIndex]
        else:
            return array[chidIndex] > array[newIndex]

    def heapify(self, currIndex, array):

        last = len(array)
        newIndex = currIndex
        left = 2 * newIndex
        right = 2 * newIndex + 1

        if left < last and self.compareHeapify(left, newIndex, array):
            newIndex = left

        if right < last and self.compareHeapify(right, newIndex, array):
            newIndex = right

        if newIndex != currIndex:
            # swap
            temp = array[newIndex]
            array[newIndex] = array[currIndex]
            array[currIndex] = temp

            self.heapify(newIndex, array)

    def convertToHeap(self, array):
        firstNonLeafNode = len(array) // 2

        curr = firstNonLeafNode
        while curr != -1:
            self.heapify(curr, array)
            curr -= 1


array = [10 ,5 ,6 ,2 ,12, 7, 9]


heap1 = Heap(True)
heap1.convertToHeap(array)
print(array)