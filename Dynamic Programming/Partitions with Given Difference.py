"""

arr1 + arr2 = total
arr1 - arr2 = diff

2arr1 = total + diff
arr1 = (total + diff) // 2

So we just need to count the number of ways we can generate this arr1 if
we possibly can
"""


class Solution:

    def count(self, currIndex, arr, target, cache):

        if currIndex == len(arr) and target == 0:
            return 1

        if currIndex == len(arr):
            return 0

        if (currIndex, target) in cache:
            return cache[(currIndex, target)]

        op1 = self.count(currIndex + 1, arr, target - arr[currIndex], cache)
        op2 = self.count(currIndex + 1, arr, target, cache)

        cache[(currIndex, target)] =  op1 + op2
        return cache[(currIndex, target)]



    def countPartitions(self, arr, diff):

        target = (sum(arr) + diff) // 2

        if target % 2 == 1:
            return 0

        return self.count(0, arr, target, cache = {})

s = Solution()
print(s.countPartitions([5, 2, 6, 4], diff = 3))
print(s.countPartitions( [1, 1, 1, 1], diff = 0 ))
print(s.countPartitions([3, 2, 5, 1], diff = 4  ))