class Solution:

    def countSubsets(self, currIndex, target, arr, cache):

        """
        We have both  the len and target check because we want to make sure a set is generated after all the
        possible combination, and we do not stop the exploration because target became zero.

        For example
        """
        if currIndex == len(arr) and target == 0:
            return 1

        if currIndex == len(arr):
            return 0

        if (currIndex, target) in cache:
            return cache[(currIndex, target)]

        if target - arr[currIndex] < 0:
            cache[(currIndex, target)] =  self.countSubsets(currIndex + 1, target, arr, cache)
            return cache[(currIndex, target)]

        op1 = self.countSubsets(currIndex + 1, target - arr[currIndex], arr, cache)
        op2 = self.countSubsets(currIndex + 1, target, arr, cache)

        cache[(currIndex, target)] = op1 + op2
        return cache[(currIndex, target)]

    def perfectSum(self, arr, target):
        return self.countSubsets(0, target, arr, cache={})

