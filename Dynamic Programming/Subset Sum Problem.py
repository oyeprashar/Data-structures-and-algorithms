class Solution:

    def subsetSumHelper(self, currIndex, target, arr, cache):

        if target == 0:
            return True

        if currIndex == len(arr):
            return False

        if (currIndex, target) in cache:
            return cache[(currIndex, target)]


        op1 = self.subsetSumHelper(currIndex + 1, target - arr[currIndex], arr, cache)
        op2 = self.subsetSumHelper(currIndex + 1, target, arr, cache)

        cache[(currIndex, target)] =  op1 or op2
        return cache[(currIndex, target)]

    def isSubsetSum(self, arr, sum):
        return self.subsetSumHelper(0, sum, arr, cache={})