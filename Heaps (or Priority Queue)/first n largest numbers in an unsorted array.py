import heapq


class Solution:

    def kLargest(self, arr, n, k):

        for i in range(len(arr)):
            arr[i] = -1 * arr[i]

        heapq.heapify(arr)  # O(N)

        ans = []

        for _ in range(k):  # O(klogn)
            ans.append(-1 * heapq.heappop(arr))

        return ans