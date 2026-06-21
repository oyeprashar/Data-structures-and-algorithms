"""
    There are n packets of chocolates
    m is the number of student
    each packet contains some number of chocolates
    We need to minimise the diff between max and min chocolate given to m student
"""

class Solution:
    def findMinDiff(self, arr, m):


        """
        So we need to select m packets and minimise the max and min
        Max and min will be closet when the arr is sorted

        1. Sort the array
        2. Have a sliding window of size m
        3. Max and min are closet and keep track of their difference for the global answer
        """

        arr.sort()
        i = 0
        j = m - 1
        min_diff = 3**38

        while j < len(arr):
            min_diff = min(min_diff, arr[j] - arr[i])
            j += 1
            i += 1

        return min_diff
