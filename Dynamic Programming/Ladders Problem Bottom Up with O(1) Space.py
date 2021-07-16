class Solution:

    def countWays(self, n):
        # <-Bottom up dp with space optimization->
        memory = [0] * (2)
        memory[0] = memory[1] = 1

        for i in range(2, n + 1):
            res = memory[0] + memory[1]
            memory[0] = memory[1]
            memory[1] = res

        return memory[1]


