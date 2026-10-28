import heapq

class Solution:

    def __init__(self):
        self.maxHeap = [] # left side
        self.minHeap = [] # right side

    def balanceHeaps(self):

        if len(self.maxHeap) > len(self.minHeap):
            heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))

        else:
            heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))


    def insertIntoHeaps(self, num):
        if len(self.maxHeap) == 0 or num <= -1 * self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -1 * num)

        else:
            heapq.heappush(self.minHeap, num)

        if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
            self.balanceHeaps()

    def fetchMedian(self):

        if len(self.maxHeap) == len(self.minHeap):
            num1 = -1 * self.maxHeap[0]
            num2 = self.minHeap[0]

            return (num1 + num2) / 2

        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]

        else:
            return self.minHeap[0]


    def getMedian(self, arr):

        # the right side
        ans = []

        for num in arr:

            self.insertIntoHeaps(num)
            ans.append(self.fetchMedian())

        return ans
