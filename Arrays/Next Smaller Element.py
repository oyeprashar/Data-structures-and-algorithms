"""
Algorithm :
    1. Since we need to find the smaller element immediate right to current element, we process from left to right
    2. In any case, we will add the element to the stack since we need it for the element on the left
    3. Remove all the elements which are bigger than current element, they cannot be the answer
    4. If there is something left on the stack, that is the answer for the current element
"""

class Solution:

    def nextSmallerEle(self, arr):

        ans = [-1] * len(arr)
        stack = []

        for i in range(len(arr) - 1, -1, -1):

            if len(stack) == 0:
                stack.append(arr[i])
                continue

            # pop the elements bigger than arr[i], they aint our answer
            while len(stack) > 0 and stack[-1] >= arr[i]:
                stack.pop(0)

            if len(stack) > 0:
                ans[i] = stack[-1]

        return ans
