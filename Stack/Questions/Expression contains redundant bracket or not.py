"""
Expression contains redundant bracket or not

((a + b)) <-- redundant
(a + b) <-- not redundant

Approach
    1. Push everything to stack if it is not a closing bracket ")"
    2. Now when we encounter a closing bracket ")" we do this :
        i. Start popping from the stack
       ii. Before we reach its opening bracket we check if there are any operators between them
      iii. If there are no operators between () then the bracket is redundant, return True
"""

class Solution():
    def checkRedundancy(self, s):

        stack = []
        operators = {"+", "-", "/", "*"}

        for i in range(len(s)):

            if s[i] != ")":
                stack.append(s[i])

            else:

                operatorFound = False

                while len(stack) > 0 and stack[-1] != "(":
                    if stack[-1] in operators:
                        operatorFound = True

                    stack.pop()

                # remove that opening bracket we were trying to find
                stack.pop()

                if not operatorFound:
                    return True

        return False

string = "(a+(b+(c+d)))"
s = Solution()
print(s.checkRedundancy(string))
