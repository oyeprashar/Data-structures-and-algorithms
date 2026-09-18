"""
    For every recursive call, we remove the outer boundary brackets
    so that currIndex is sitting at some int and not a bracket

    Example:
        4(2(3)(1))(6(5))

    Left subtree:
        (2(3)(1)) -> 2(3)(1)

    Right subtree:
        (6(5))    -> 6(5)

    Since currIndex is sitting at some int, the last bracket is not balancing anything and we exclude it as well
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:


    def getClosingBracketIndex(self, start, end, string):

        if start > end:
            return -1

        count = 0

        for i in range(start, end + 1):

            if string[i] == '(':
                count += 1

            elif string[i] == ')':
                count -= 1

            if count == 0:
                return i

        return -1


    def generateTree(self, left, right, string):

        if left > right:
            return None

        # we need to handle the case where the num is more than 1 digit
        value = 0

        while left <= right and string[left].isdigit():
            value *= 10 # to place the current int at the right digit
            value += int(string[left])
            left += 1

        # now left is sitting on a non-int value i.e. a bracket

        root = Node(value)

        # Now we have to figure out if there is a left and right
        # subtree connected to this root node or not

        endIndex = -1

        if left <= right and string[left] == '(':
            endIndex = self.getClosingBracketIndex(left, right, string)

        # if subtree were found
        if endIndex != -1:

            # left is at a bracket and endIndex is at a bracket
            # the exclusion logic is explained at the start of the file
            root.left = self.generateTree(left + 1, endIndex - 1, string)
            root.right = self.generateTree(endIndex + 2, right - 1, string)

        return root


    def treeFromString(self, s):
        return self.generateTree(0, len(s) - 1, s)
