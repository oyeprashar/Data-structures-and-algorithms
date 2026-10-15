"""

The question is asking us to find the longest length that is balanced. We simulate exactly the same.


We already know the code for balancing brackets in a string, now we make the following changes to that code. Now, we
need to make it smarter such that we always know what length a closing bracket balances


  Algorithm

      The stack is initiated with -1 as if the whole string is balanced, we calculate the length of the whole string

      1. Save the index of the opening bracket
      2. When a closing bracket comes, we pop the element from the stack and then the length is computed with the stack top
         this stack top acts as a boundary
      NOTE : The len is NOT computed with what we popped and rather with the stack top
      3. If a closing bracket makes the stack empty, then it means it is a new boundary as it is invalid and we append this
      to the stack
"""


class Solution:
    def maxLength(self, bracketString):

        stack = [-1]
        maxLen = 0

        for index, bracket in enumerate(bracketString):

            if bracket == "(":
                stack.append(index)
            else:
                stack.pop()

                #### TODO : write about this case! This is very special
                if len(stack) == 0:
                    stack.append(index)

                else:
                    maxLen = max(maxLen, index - stack[-1])

        return maxLen


s = Solution()
print(s.maxLength("(()())"))