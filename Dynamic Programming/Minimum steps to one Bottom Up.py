"""
This is Bottom Up approach where we find solution of the smallest problem and build the res of the given input using a loop
TIME COMPLEXITY = O(N) | SPACE COMPLEXITY = O(N)
"""
class Solution:
    def minSteps(self, N):

        mem = [-1] * (N + 1)
        mem[1] = 0

        for i in range(2, N + 1):
            res1 = res2 = res3 = 3 ** 38

            if i % 2 == 0:
                res1 = mem[i // 2]

            if i % 3 == 0:
                res2 = mem[i // 3]

            res3 = mem[i - 1]

            mem[i] = min(res1, res2, res3) + 1

        return mem[N]