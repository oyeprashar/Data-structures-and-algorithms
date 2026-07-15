"""
    Approach :
        - Recursively remove elements from the stack until there is no more element
        - Now insert the element st index zero goes to the end of the stack
"""

class Solution:

    # Now insert the element st index zero goes to the end of the stack
    def insertAtStart(self, stack, num):

        # We want to insert the element at the bottom

        # if no elements are there in the stack then append the element
        if len(stack) == 0:
            stack.append(num)
            return

        # remove the elements
        top  = stack.pop()
        self.insertAtStart(stack, num)

        # add the element back in the order they were
        stack.append(top)


    # Recursively remove elements from the stack until there is no more element
    def reverseStackHelper(self, stack):

        if len(stack) == 0:
            return

        top = stack.pop()
        self.reverseStackHelper(stack)

        # now we have the first element, and we want to insert it at the bottom of the stack
        self.insertAtStart(stack, top)

        # insert it at the last of the stack

    # O(n^2)
    def reverseStack(self, stack):
        self.reverseStackHelper(stack)
        return stack

s = Solution()
print(s.reverseStack([1, 2, 3, 4, 5, 6]))
