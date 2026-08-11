class Solution:

    # Function to find maximum
    # product subarray
    def maxProduct(self, arr):

        """
        A neg number makes the largest number smallest and the smallest number largest so we need to keep track of
        both max and min sum and when a neg number comes we swap them!
        """

        maxProduct = arr[0]
        minProduct = arr[0]
        res = arr[0]

        for i in range(1, len(arr)):

            if arr[i] < 0:
                maxProduct, minProduct = minProduct, maxProduct

            maxProduct = max(maxProduct * arr[i], arr[i])
            minProduct = min(minProduct * arr[i], arr[i])

            res = max(res, maxProduct)

        return res


