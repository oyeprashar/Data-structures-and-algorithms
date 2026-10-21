"""
Approach :
    1. The deque will contain indices
    2. in a while loop, remove the elements outside the window
    3. if the incoming element is greater than element in deque (from the last), then we pop these element in a
        while loop as these elements are not useful to us
    4. Once the first window is processed, we can start adding answer to ans


The way we used deque for sliding the window is a pattern which we have seen on other problems as well. The generic version
    - To maintain the size, check the index stored at 0th index of dq with <= currIndex - window size
    - Remove elements which are invalid due to current element
    - Save the answer from the windw

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

            # remove the smaller elements as they are not useful once
            # a bigger element comes
            while len(dq) > 0 and arr[dq[-1]] <= arr[i]:
                dq.pop()

            # append the current index
            dq.append(i)

            if i >= k - 1:
                ans.append(arr[dq[0]])

        return ans
