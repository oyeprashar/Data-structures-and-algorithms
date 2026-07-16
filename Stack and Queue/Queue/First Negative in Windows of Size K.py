from collections import deque

class Solution:
    def firstNegInt(self, arr, k):
        dq = deque()
        ans = []
        for i in range(len(arr)):

            # append the indices were the neg elements are
            if arr[i] < 0:
                dq.append(i)

            # remove the indices that are out of the current window
            if len(dq) > 0 and dq[0] <= i - k:
                dq.popleft()

            # Once the first window is formed, process every window
            # because after the first window, the window is sliding where one element is removed and another is added to the window
            if i >= k - 1:
                if len(dq) == 0:
                    ans.append(0)
                else:
                    ans.append(dq[0])

        return ans
