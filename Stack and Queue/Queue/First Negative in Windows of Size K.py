"""
Algorithm  :
    1. Add the neg index in the deque
    2. since we are storing indices, check is the index at index 0 of dequeue is out of bounds if it is <= currIndex - k
    3. We start storing the answers after the first window is crossed
"""

from collections import deque

class Solution:

    def firstNegInt(self, arr, k):

        dq = deque([])
        ans = []

        for i in range(len(arr)):

            # push the index of neg element into the deque
            if arr[i] < 0:
                dq.append(i)

            # if len(deque) is more k, remove the left most
            # i is current index
            # k is the size of window
            # current current index - window size == the index just outside the window
            if len(dq) > 0 and dq[0] <= i - k:
                dq.popleft()

            if i >= k - 1:

                if len(dq) == 0:
                    ans.append(0)
                else:
                    ans.append(dq[0])

        return ans
