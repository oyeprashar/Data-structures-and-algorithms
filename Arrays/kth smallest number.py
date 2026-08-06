import heapq


class Solution:
    def kthSmallest(self, arr, k):

        """
        - We will keep a heap of size k
        - We will always remove the top of the max heap when the size of max_heap > k
        - This helps us to maintain k smallest elements!
        - Removing the top is helpful because when the size of heap is k + 1 then the max element is not useful
        """

        maxHeap = []


        # TC : O(nlogk)
        # since the size of max heap is restricted to k, operation over it is O(logk) and we process all the in O(n)
        for i in range(len(arr)):

            heapq.heappush(maxHeap, -1 * arr[i])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return - 1 * heapq.heappop(maxHeap)
