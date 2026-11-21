"""
Input: val[] = [1, 1], wt[] = [2, 1], capacity = 3
Output: 3
"""


class Solution:

    def unboundedKnapsack(self, currIndex, values, weights, capacity, cache):

        if capacity == 0 or currIndex == len(values):
            return 0

        if capacity - weights[currIndex] < 0:
            cache[(currIndex, capacity)] = self.unboundedKnapsack(currIndex + 1, values, weights, capacity, cache)
            return cache[(currIndex, capacity)]


        if (currIndex, capacity) in cache:
            return cache[(currIndex, capacity)]

        op1 = values[currIndex] + self.unboundedKnapsack(currIndex, values, weights, capacity - weights[currIndex], cache)
        op2 = self.unboundedKnapsack(currIndex + 1, values, weights, capacity, cache)

        cache[(currIndex, capacity)] = max(op1, op2)
        return cache[(currIndex, capacity)]


    def knapSack(self, values, weights, capacity):
        # code here
        return self.unboundedKnapsack(0,  values, weights, capacity, cache = {})


s = Solution()
print(s.knapSack(values = [1, 1], weights = [2, 1], capacity = 3))
print(s.knapSack(values = [10, 40, 50, 70], weights = [1, 3, 4, 5], capacity = 8))