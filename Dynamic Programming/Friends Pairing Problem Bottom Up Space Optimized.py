# TIME COMPLEXITY: O(N) | SPACE COMPLEXITY: O(1)
class Solution:
    def countFriendsPairings(self, n):

        if n == 0 or n == 1 or n == 2:
            return n

        memory = [1] * 2
        memory[1] = 2

        for i in range(3, n + 1):
            res = memory[1] + (i - 1) * memory[0]  # % 1000000007
            memory[0] = memory[1] % 1000000007
            memory[1] = res % 1000000007

        return memory[1]