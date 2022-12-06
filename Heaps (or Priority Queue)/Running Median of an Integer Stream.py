# User function Template for python3
global min_heap
min_heap = []
global max_heap
max_heap = []


class Solution:
    def balanceHeaps(self):

        if len(max_heap) > len(min_heap) + 1:
            topElement = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -1 * topElement)
        elif len(min_heap) > len(max_heap) + 1:
            topElement = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -1 * topElement)

    def getMedian(self):

        if len(max_heap) > len(min_heap):
            currMedian = -1 * max_heap[0]
            return currMedian
        elif len(min_heap) > len(max_heap):
            currMedian = min_heap[0]
            return currMedian
        elif len(max_heap) == len(min_heap):
            currMedian = (-1 * max_heap[0] + min_heap[0]) // 2 # NOTE: if the test case wants integer values then use '//'
            return currMedian                                  #       else use '/' to get float values

    def insertHeaps(self, x):

        if len(max_heap) == 0 or -1 * max_heap[0] > x:
            heapq.heappush(max_heap, -1 * x)
        else:
            heapq.heappush(min_heap, x)


