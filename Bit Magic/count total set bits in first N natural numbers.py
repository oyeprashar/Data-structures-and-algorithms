import math

class Solution:

    def countSetBits(self, n):
        if n == 0:
            return 0

        x = int(math.log(n, 2))

        return int((2 ** (x - 1) * x) + (n - (2 ** x) + 1) + self.countSetBits(n - 2 ** x))

s = Solution()
print(s.countSetBits(11))