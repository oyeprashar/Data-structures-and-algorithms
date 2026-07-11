"""
Approach is simple!
    - Count the number of invalid brackets at each step
    - Remove brackets from the string
    - if number of removals needed == 0 and invalid brackets == 0, save it!
    - Memoisation to skip already processed strings!
"""


class Solution:

    # O(N)
    def countBracketsCausingImbalance(self, string):

        stack = []
        for bracket in string:

            if bracket not in "()":
                continue

            if bracket == "(":
                stack.append(bracket)
            else:
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(bracket)

        return len(stack)

    def generateBracketStrings(self, string, numberOfRemovals, ans, visited):

        # memoisation!
        if string in visited:
            return

        # we found a valid string
        if numberOfRemovals == 0 and self.countBracketsCausingImbalance(string) == 0:
            ans.add(string)
            return

        if numberOfRemovals == 0:
            return

        for i in range(len(string)):
            if string[i] in "()":
                newString = string[:i] + string[i+1:] # this is slicing and not direct indexing, so even when i >= len(s), no error is thrown and "" is returned
                self.generateBracketStrings(newString, numberOfRemovals - 1, ans, visited)

        visited.add(string)

    # O(n^2)
    def removeInvalidParentheses(self, s):
        minRemoval = self.countBracketsCausingImbalance(s)
        ans = set()
        self.generateBracketStrings(s, minRemoval, ans, visited = set())
        return list(ans)

s = Solution()
print(s.removeInvalidParentheses("()())()"))
print(s.removeInvalidParentheses("(a)())()"))  # This is wrong
print(s.removeInvalidParentheses(")("))
