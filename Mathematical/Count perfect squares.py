"""
search space consists of all perfect squares i.e. [1, 4, 9............]
given integer N, find all the number of perfect squares before N 
"""

import math

class Solution:
    def countSquares(self, N):
        x = int(math.sqrt(N))
        if x*x == N:
            return x-1
        else:
            return x
        
