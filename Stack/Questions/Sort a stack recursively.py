"""
Time complexity : O(N^2)

This is because everytime a call returns from the recursion stack, we can go and remove element from the stack so n*n
"""

class Solution:
    def sortStack(self, stack):

        if len(stack) == 0:
            return

        top = stack.pop()
        self.sortStack(stack)

        if len(stack) == 0 or top >= stack[-1]:
            stack.append(top)

        else:
            poppedStack = []

            while len(stack) > 0 and top < stack[-1]:
                poppedStack.append(stack.pop())

            stack.append(top)

            while len(poppedStack) > 0:
                stack.append(poppedStack.pop())

        return stack
