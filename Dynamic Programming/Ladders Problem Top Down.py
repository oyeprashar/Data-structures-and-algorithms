# TIME COMPLEXITY = O(N*K) | SPACE COMPLEXITY : O(N)
class Solution:
    # <-TOP DOWN DP ->
    def countSteps(self, curr, N, k, memory):
        if curr == N:
            return 1

        if curr > N:
            return 0

        if memory[curr] != -1:
            return memory[curr]

        res = 0

        for step in range(1, k + 1):
            res += self.countSteps(curr + step, N, k, memory)
        memory[curr] = res

        return res

