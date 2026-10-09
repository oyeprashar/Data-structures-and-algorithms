"""
Time complexity : O(2^n) since we have 2 options at each index (more than that actually since elements can repeat)
"""

class Solution:

    def generateSubset(self, currIndex, arr, target, currSet, res):

        if target == 0:
            res.append(currSet.copy())
            return

        if currIndex >= len(arr):
            return

        # skip if this element over shoots the target value
        if target - arr[currIndex] < 0:
            return self.generateSubset(currIndex + 1, arr, target, currSet, res)

        # we have two options, either we choose or we dont

        currSet.append(arr[currIndex])
        self.generateSubset(currIndex, arr, target - arr[currIndex], currSet, res)
        currSet.pop()

        self.generateSubset(currIndex + 1, arr, target, currSet, res)


    def targetSumComb(self, arr, target):
        res = []
        self.generateSubset(0, arr, target, [], res)
        return res

s = Solution()
print(s.targetSumComb(arr = [1, 2, 3], target = 5))