import heapq

class Solution:
    def kthLargest(self, k, arr, n):
        min_heap = []
        ans = []
        for item in arr:
            # this section is for pushing item
            if len(min_heap) < k:
                heapq.heappush(min_heap, item)

            elif len(min_heap) == k and item > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, item)

            # this section is for appending kth largest in stream to our ans

            if len(min_heap) < k:
                ans.append(str(-1))

            elif len(min_heap) == k:
                ans.append(str(min_heap[0]))

        return " ".join(ans)
