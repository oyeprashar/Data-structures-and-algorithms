"""
    Input: arr[] = [1, 3, 2, 4]
    Output: [3, 4, 4, -1]
    Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.
"""

class Solution:

    def nextLargerElement(self, arr):

        stack = []

        ans = []
        minSoFar = arr[-1]

        for i in range(len(arr) -1, -1, -1):


            while len(stack) > 0 and stack[-1] < arr[i]:
                stack.pop()

            if len(stack) == 0:
                ans.append(-1)
            else:
                ans.append(stack[-1])

            stack.append(arr[i])

        return ans[::-1]


s = Solution()
print(s.nextLargerElement(arr = [6, 8, 0, 1, 3]))
# [8, -1, 1, 3, -1]


