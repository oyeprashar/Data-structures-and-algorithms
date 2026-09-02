class Solution:
    def findStepKeyIndex(self, arr, stepSize, target):

        i = 0

        while i < len(arr):

            if arr[i] == target:
                return i

            # This helps us understand the indices which we can safely skip
            safeToJump = abs(arr[i] - target) // stepSize

            i += max(1, safeToJump) # in case safe to jump is zero, taking max with 1 moves us to the next index

        return -1

