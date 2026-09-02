"""
    Input: sum = 2, arr[] = [-2, 0, 1, 3]
    Output:  2
    Explanation: Triplets with sum less than 2 are (-2, 0, 1) and (-2, 0, 3).

    Input: sum = 12, arr[] = [5, 1, 3, 4, 7]
    Output: 4
    Explanation: Triplets with sum less than 12 are (1, 3, 4), (5, 1, 3), (1, 3, 7) and (5, 1, 4).
"""


class Solution:

    def countTriplets(self, targetSum, arr):

        arr.sort()
        count = 0

        for i in range(len(arr) - 1):
            j = i + 1
            k = len(arr) - 1

            while j < k:

                """
                If arr[i] + arr[j] + arr[k] < targetSum, then since the array is sorted,
                for the fixed pair (i, j), every element from index j + 1 through k
                can be chosen as the third element.

                There are (k - j) such choices, so we add that many triplets.
                """

                currSum = arr[i] + arr[j] + arr[k]

                if currSum < targetSum:
                    count += (k - j)
                    j += 1

                else:
                    k -= 1

        return count


s = Solution()
print(s.countTriplets(2, [-2, 0, 1, 3]))
print(s.countTriplets(12, [5, 1, 3, 4, 7]))








