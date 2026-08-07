"""
Approach :
    - We want to process one chunk at a time
    - When i == jumpTill, we re-initialise jumpTill with the farthest that we found in the last chunk
    - We process chunk by chunk because in jump game - 2 we need to return the min jumps and processing chunks is
        how we can minimise the jumps
"""


class Solution:
    def canJump(self, nums):

        farthest = 0 # keep track of farthest we can reach
        jumpTill = 0 # Used to process one chunk at a time

        for i in range(len(nums)):

            # index is out of reach!
            if i > farthest:
                return False

            farthest = max(farthest, i + nums[i])

            if i == jumpTill:
                jumpTill = farthest

        return True
