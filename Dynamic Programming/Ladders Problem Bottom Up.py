class Solution:

    def countWays(self, n):
        # <-Bottom up dp with no space optimization->
        memory = [0] * (n + 1)
        memory[0] = memory[1] = 1

        for i in range(2, len(memory)):
            memory[i] = memory[i - 1] + memory[i - 2]

        return memory[n]

