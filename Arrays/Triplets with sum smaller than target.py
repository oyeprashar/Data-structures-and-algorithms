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

        for i in range(len(arr)-2):

            j = i + 1
            k = len(arr) - 1

            while j < k:

                if arr[i] + arr[j] + arr[k] < targetSum:

                    """
                    when we find arr[i] + arr[j] + arr[k] < k and array is sorted that means elements from i + 1 till k
                    can pair up with i and j to form the triplets having sum less than target
                    
                    so i, j can pair with (k-j) elements and we add that count to answer
                    """
                    count += (k - j)

                    # This is because we already counted elements (k-j) with i, j and if we decrement k, it won't be useful
                    # So We increment j to find new combinations with j
                    j += 1

                else:
                    k -= 1

        return count

s = Solution()
print(s.countTriplets(2, [-2, 0, 1, 3]))
print(s.countTriplets(12, [5, 1, 3, 4, 7]))








