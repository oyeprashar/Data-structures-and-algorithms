"""
Approach :
    1. The deque will contain indices
    2. in a while loop, remove the elements outside the window
    3. if the incoming element is greater than element in deque (from the last), then we pop these element in a
        while loop as these elements are not useful to us
    4. Once the first window is processed, we can start adding answer to ans
"""

from collections import deque

class Solution:

    def maxOfSubarrays(self, arr, k):

        # the deque should contain elements in ascending order
        dq = deque()
        ans = []

        for i in range(len(arr)):

            # remove indices outside current window
            while len(dq) > 0 and dq[0] <= i - k:
                dq.popleft()

            # remove the smaller elements
            while len(dq) > 0 and arr[dq[-1]] <= arr[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                ans.append(arr[dq[0]])

        return ans
