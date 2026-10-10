"""
We need to do at most k swaps and generate the largest number so there are two options at every index. Either we move
ahead without doing anything or we swap. And we need to return the max of these two options


    Algorithm

        Steps for op1:
            1.Simply don't do anything and move ahead

        Steps for op2 :
            1. Find the number that is greatest (than the current index element)
            2. Swap with each of these (at every index)
            3. While doing this figure out the largest op2

        return max(op1, op2)

    Time complexity analysis :
        - There are n options at every n index so = O(n^n)
        - We are running a loop everytime to find greatest = O(n)
        - Total : O(n^n * n)
        """
INT_MIN = -3 ** 38


class Solution:

    def convertToInt(self, arr):

        p = 1
        num = 0

        for i in range(len(arr) - 1, -1, -1):
            num += p * int(arr[i])
            p *= 10

        return num

    def findMaximumNumHelper(self, currIndex, arr, k, res):

        if k == 0 or currIndex == len(arr):
            return self.convertToInt(arr)

        # We dont process the current digit
        op1 = self.findMaximumNumHelper(currIndex + 1, arr, k, res)
        op2 = INT_MIN


        """
        Steps for op2 :
            1. Find the number that is greatest (than the current index element)
            2. Swap with each of these (at every index)
            3. While doing this figure out the largest op2
        """
        greatestNumber = int(arr[currIndex])

        for i in range(currIndex, len(arr)):

            if int(arr[i]) > greatestNumber:
                greatestNumber = int(arr[i])


        if greatestNumber != int(arr[currIndex]):

            for i in range(currIndex, len(arr)):

                if int(arr[i]) == greatestNumber:

                    arr[currIndex], arr[i] = arr[i], arr[currIndex]
                    num = self.findMaximumNumHelper(currIndex + 1, arr, k-1, res)
                    op2 = max(op2, num)
                    arr[currIndex], arr[i] = arr[i], arr[currIndex]


        return max(op1, op2)

    def findMaximumNum(self, s, k):
        res = [INT_MIN]
        arr = list(s)
        return self.findMaximumNumHelper(0, arr, k, res)

s = Solution()
print(s.findMaximumNum(s = "1234567", k = 4))



