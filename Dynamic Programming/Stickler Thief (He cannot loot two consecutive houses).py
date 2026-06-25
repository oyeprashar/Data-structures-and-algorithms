"""
Input: arr[] = [6, 7, 1, 3, 8, 2, 4]
Output: 19
Explanation: Maximum amount he can get by looting 1st, 3rd, 5th and 7th house, which is 6 + 1 + 8 + 4 = 19.
"""


class Solution:

    def findMaxSumHelper(self, currIndex, arr, memory):

        if currIndex >= len(arr):
            return 0

        if memory[currIndex]  != -1:
            return memory[currIndex]

        op1 = arr[currIndex] + self.findMaxSumHelper(currIndex + 2, arr, memory)
        op2 = self.findMaxSumHelper(currIndex + 1, arr, memory)

        memory[currIndex] = max(op1, op2)
        return memory[currIndex]

    # O(n)
    def findMaxSum(self, arr):
        memory = [-1] * len(arr)
        return self.findMaxSumHelper(0, arr, memory)

s = Solution()
print(s.findMaxSum([5, 3, 4, 11, 2]))
