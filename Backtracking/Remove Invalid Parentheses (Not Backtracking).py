"""
Approach is simple!
    - Count the number of invalid brackets at each step
    - Remove brackets from the string
    - if number of removals needed == 0 and invalid brackets == 0, save it!
    - Memoisation to skip already processed strings!


Time complexity :
    - O(2^n) because at every index we have 2 options of removing or not removing the bracket
    - O(n +n) for numberOfImblancedBrackets(string) and slicing
    - total O(2^n *n)
"""


class Solution:

    def numberOfImblancedBrackets(self, string):

        stack = []

        for bracket in string:

            if bracket not in "()":
                continue

            if bracket == "(":
                stack.append("(")
            else:

                if len(stack) == 0 or stack[-1] != '(':
                    stack.append(bracket)
                else:
                    stack.pop()

        return len(stack)


    def removeInvalidParenthesesHelper(self, string, numberOfRemovalsLeft, res, visited):

        # The string is duplicate to a string we already processed
        if string in visited:
            return

        # we found a valid representation
        if numberOfRemovalsLeft == 0 and self.numberOfImblancedBrackets(string) == 0:
            res.add(string)
            return

        if numberOfRemovalsLeft == 0:
            return

        for i in range(len(string)):
            newString = string[:i] + string[i + 1:]
            self.removeInvalidParenthesesHelper(newString, numberOfRemovalsLeft - 1, res, visited)

        # I have now finished exploring every possible recursive path that can originate from this string
        # so mark this string as completely processed.
        visited.add(string)

    def removeInvalidParentheses(self, string):
        res = set()
        self.removeInvalidParenthesesHelper(string, self.numberOfImblancedBrackets(string), res, set())
        return list(res)


s = Solution()
print(s.removeInvalidParentheses("()())()"))
