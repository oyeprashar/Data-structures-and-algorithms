"""
Here we don't count the jumps from the last index because

    1. It is given that the last index is reachable
    2 There can be a case where the chunk ends at the last index and we start a new chunk from it returning a wrong ans
"""


class Solution:

    def jump(self, nums):

        farthest = 0  # keep track of farthest we can reach
        jumpTill = 0  # Used to process one chunk at a time
        jumps = 0

        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            if i == jumpTill:
                jumpTill = farthest
                jumps += 1

        return jumps




