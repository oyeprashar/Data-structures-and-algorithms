"""
This is the top down approach
-> We still solve using recursion but now we save the subproblems as we break down the problem into subproblems and compute them
TIME COMPLEXITY = O(N) | SPACE COMPLEXITY = O(N)
"""


class Solution:
    def minStepsHelper(self, N, mem):

        if N == 1:
            return 0

        if mem[N] != -1:
            return mem[N]

        res1 = res2 = res3 = 3 ** 38

        if N % 2 == 0:
            res1 = self.minStepsHelper(N // 2, mem)

        if N % 3 == 0:
            res2 = self.minStepsHelper(N // 3, mem)

        res3 = self.minStepsHelper(N - 1, mem)

        ans = min(res1, res2, res3) + 1
        mem[N] = ans

        return ans

        def minSteps(self, N):

            if N == 0:
                return 0
                mem = [-1] * (N + 1)
                mem[1] = 0
            self.minStepsHelper(N, mem)
            return mem[N]
