"""
Reverse a stack recursively

Time complexity is O(n^2) since we are iterating the array in both the methods and they are nested
"""


class Solution:


    def insertAtABottom(self, element, stack):

        # bottom reached, we put the element here
        if len(stack) == 0:
            stack.append(element)
            return

        # save the element to put back while calls get returned so they go back to their original ordering
        stackElement = stack.pop()
        self.insertAtABottom(element, stack)
        stack.append(stackElement)


    """
    The idea is to remove an element and then put it in the start effectively reversing the stack
    """
    def reverseStackRecursion(self, stack):

        if len(stack) == 0:
            return

        element = stack.pop()
        self.reverseStackRecursion(stack)
        self.insertAtABottom(element, stack)



    def reverseStack(self, st):
        self.reverseStackRecursion(st)
        return st

s = Solution()

# stack = [1, 2, 3, 4]
# s.insertAtABottom(5, stack)
# print(stack)

print(s.reverseStack(st = [1, 2, 3, 4]))
