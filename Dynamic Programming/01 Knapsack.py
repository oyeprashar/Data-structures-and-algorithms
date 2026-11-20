"""
let N = len(values) or number of items
let capacity be C

then total size of cache table is N * C and work done at each call is O(1)

Time complexity is : O(N*C)
"""

class Solution:

    def knapsack01(self, currIndex,  values, weights, capacity, cache):

        if (currIndex, capacity) in cache:
            return cache[(currIndex, capacity)]

        if currIndex >= len(values):
            return 0

        if capacity - weights[currIndex] < 0:
            cache[(currIndex, capacity)] = self.knapsack01(currIndex + 1, values, weights, capacity, cache)
            return cache[(currIndex, capacity)]

        op1 = values[currIndex] + self.knapsack01(currIndex + 1, values, weights, capacity - weights[currIndex], cache)
        op2 = self.knapsack01(currIndex + 1, values, weights, capacity, cache)

        cache[(currIndex, capacity)] = max(op1, op2)
        return cache[(currIndex, capacity)]


    def knapsack(self, capacity, values, weights):
        return self.knapsack01(0, values, weights, capacity, cache={})