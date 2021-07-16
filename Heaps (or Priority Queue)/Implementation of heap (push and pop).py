class Heap:
    def __init__(self, type1=False):
        self.array = []
        self.type1 = type1

    def pushCompare(self, currIndex, parentIndex):
        if self.type1 is False:
            return self.array[parentIndex] > self.array[currIndex]
        else:
            return self.array[parentIndex] < self.array[currIndex]

    def push(self, item):
        self.array.append(item)
        currIndex = len(self.array) - 1
        parentIndex = currIndex // 2

        while currIndex != 0 and self.pushCompare(currIndex, parentIndex):
            # swap the elements
            temp = self.array[parentIndex]
            self.array[parentIndex] = self.array[currIndex]
            self.array[currIndex] = temp

            # new indices
            currIndex = parentIndex
            parentIndex = currIndex // 2

    def heapifyCompare(self, childIndex, parentIndex):
        if self.type1 is False:
            return self.array[childIndex] < self.array[parentIndex]
        else:
            return self.array[childIndex] > self.array[parentIndex]

    def heapify(self, currIndex):
        last = len(self.array) - 1
        newIndex = currIndex
        left = 2 * newIndex
        right = 2 * newIndex + 1

        if left <= last and self.heapifyCompare(left, newIndex):
            newIndex = left

        if right <= last and self.heapifyCompare(right, newIndex):
            newIndex = right

        if newIndex != currIndex: # if we found a new parent
            # swap
            temp = self.array[newIndex]
            self.array[newIndex] = self.array[currIndex]
            self.array[currIndex] = temp

            # heapify the newIndex
            self.heapify(newIndex)

    def pop(self):
        """
        -> swap element at index 0 with the last index
        -> heapify the element at index 1
        -> Note: we swap the 0th index and the last index because if we dont do so and just pop the 0th index then every element of the array has to move one position to the left
                 which would cost O(N) time, to save this time we swap the 0th index with the last index and heapify the 1st index. This will just cost us O(logN) time for heapify
        """
        # swapping
        last = len(self.array) - 1
        temp = self.array[0]
        self.array[0] = self.array[last]
        self.array[last] = temp
        popped = self.array.pop()

        # heapfiy the element at index 0
        self.heapify(0)

        return popped


minHeap = Heap()
minHeap.push(110)
minHeap.push(100)
# minHeap.push(3)
# minHeap.push(200)
print(minHeap.array)
print(minHeap.pop())
print(minHeap.array)