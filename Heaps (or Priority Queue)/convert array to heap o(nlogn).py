"""
ALGORITHM TO CONVERT ARRAY TO HEAP IN O(N*LOGN)
    ->Compare the current index with its parent
    ->While the heap condition is not true or curr is not equal to 0, swap the elements and change the indices for next iteration
"""
class Heap:
    def __init__(self, type1=False):
        self.type1 = type1
        self.array = []

    def compare(self, currIndex, parentIndex):
        if self.type1 is False:
            return inputArray[currIndex] < inputArray[parentIndex]
        else:
            return inputArray[currIndex] > inputArray[parentIndex]

    def convertToHeap(self,inputArray):
        for i in range(len(inputArray)):
            currIndex = i
            parentIndex = i // 2

            while currIndex != 0 and self.compare(currIndex, parentIndex):
                temp = inputArray[currIndex]
                inputArray[currIndex] = inputArray[parentIndex]
                inputArray[parentIndex] = temp
                currIndex = parentIndex
                parentIndex = currIndex // 2

        return inputArray


h1 = Heap(True)
inputArray = [4, 1, 3, 7, 8, 17, 2, 9, 10]
minHeap = h1.convertToHeap(inputArray)
print(minHeap)
h2 = Heap()
maxHeap = h2.convertToHeap(inputArray)
print(maxHeap)


