"""
The reason why we return INT_MIN as maxValue and INT_Max as minValue when we encounter None is because when the call gets
returned to the leaf node and we check `root.data > leftMaxValue and root.data < rightMinValue` we want it to pass!



"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

INT_MAX = 3**38
INT_MIN = -3**38

class Solution:

    def largestBSTHelper(self, root, minValue, maxValue):

        if root is None:
            return True, 0, INT_MAX, INT_MIN # because the min and max is used to validate the leaf nodes

        isLeftBST, leftSize, leftMinValue, leftMaxValue = self.largestBSTHelper(root.left, minValue, maxValue)
        isRightBST, rightSize, rightMinValue, rightMaxValue = self.largestBSTHelper(root.right, minValue, maxValue)

        if isLeftBST is True and isRightBST is True and root.data > leftMaxValue and root.data < rightMinValue:

            if leftMinValue == INT_MAX:
                leftMinValue = root.data

            if rightMaxValue == INT_MIN:
                rightMaxValue = root.data

            return True, leftSize + 1 + rightSize, leftMinValue, rightMaxValue

        else:
            return False, max(leftSize, rightSize), -1, -1

    def largestBst(self, root):
        _, maxBSTSize, _, _ = self.largestBSTHelper(root, minValue=INT_MAX, maxValue=INT_MIN)
        return maxBSTSize

# Test code
root = Node(6)
root.left = Node(7)
root.left.right = Node(2)
root.right = Node(3)
root.right.left = Node(2)
root.right.right = Node(4)
s = Solution()
print(s.largestBst(root))
