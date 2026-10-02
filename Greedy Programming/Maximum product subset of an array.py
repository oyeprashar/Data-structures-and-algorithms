class Solution:

    def maximizeSum(self, arr, k):

        arr.sort()

        """
        Where to use the negations?
            The smallest neg numbers

        We must do k flips that's the rule

        """

        index = 0
        negCount = 0

        while index < len(arr) and negCount < k:

            if arr[index] < 0:
                arr[index] *= -1
                negCount += 1

        """
        1. If no negations are required then we just return the sum of the array
        2. If even number of negations are needed then we use them to neg the same number twice and keep the sum largest


        """
        if negCount == k or (k - negCount) % 2 == 0:
            return sum(arr)

        """
        if the code came till this line that means the number of required negations is negative. We do one negation on
        the smallest number and rest if wasted by negating same number twice!
        """

        arr.sort()
        arr[0] *= -1

        return sum(arr)

