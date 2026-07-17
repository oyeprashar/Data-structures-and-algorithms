"""
Form two numbers using all the digits such that their sum is minimized.

Approach:
    - We know that a number is small when the left most bit is small
    - We sort the array and form two numbers such that the left most bit is minimised
"""

import sys
sys.set_int_max_str_digits(1000000)


class Solution:

    def minSum(self, arr):
        if len(arr) == 1:
            return arr[0]

        arr.sort()
        num1 = ""
        num2 = ""

        for i in range(len(arr)):

            if i % 2 == 0:
                num1 += str(arr[i])
            else:
                num2 += str(arr[i])

        return int(num1) + int(num2)
