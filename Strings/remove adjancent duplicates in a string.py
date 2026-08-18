"""

    Input: s = "aabb"
    Output: "ab"
    Explanation: The character 'a' at index 2 is the same as 'a' at index 1, so it is removed.Similarly, the character 'b' at index 4 is the same as 'b' at index 3, so it is removed. The final string is "ab".
"""
class Solution:
    def removeDuplicates(self, string):

        stack = []
        stringList = list(string)


        for char in stringList:

            while len(stack) > 0 and stack[-1] == char:
                stack.pop()

            stack.append(char)

        return "".join(stack)



s = Solution()
print(s.removeDuplicates("aabb"))