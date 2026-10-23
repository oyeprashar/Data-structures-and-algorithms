"""
The logic is that we maintain a min heap of size k and keep removing the top (min) element effectively leaving us with
k-largest elements

Time complexity : O(nlogk)
"""

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