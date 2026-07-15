"""
    problem statement : We need to find the max length of string where the brackets are balanced
    Approach :
        - We start balancing the brackets
        - We save the index of last balanced substring (stack gets empty)
        - We use that to compute the length when a substring is balanced
        - return the max len
"""


class Solution:
    def maxLength(self, bracketString):

        # we initialise stack with -1 because let's say the whole string was balanced then
        # maxLen = lastIndex - (-1) = lastIndex + 1 = correct ans!
        stack = [-1]
        maxLen = 0

        for i in range(len(bracketString)):

            # save these indices
            if bracketString[i] == "(":
                stack.append(i)

            # if bracket is ) then pop from stack
            else:
                stack.pop()

                # can happen by alot of unbalanced closing brackets
                if len(stack) == 0:
                    # we need to save at what index this happened
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i - stack[-1])

        return maxLen
