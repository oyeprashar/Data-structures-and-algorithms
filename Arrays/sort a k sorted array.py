import heapq


class Solution:
    def nearlySorted(self, arr, k):

        minHeap = []
        res = []

        # this is k + 1 because lets say k = 2 then the element at 0 can be 0 + 2 i.e. till index 2
        for i in range(k + 1):
            heapq.heappush(minHeap, arr[i])

        for i in range(k + 1, len(arr)):
            res.append(heapq.heappop(minHeap))
            heapq.heappush(minHeap, arr[i])

        while minHeap:
            res.append(heapq.heappop(minHeap))

        for i in range(len(arr)):
            arr[i] = res[i]

        return arr