"""
The reason why we return INT_MIN as maxValue and INT_Max as minValue when we encounter None is because when the call gets
returned to the leaf node and we check `root.data > leftMaxValue and root.data < rightMinValue` we want it to pass!



"""

INT_MAX = 3**38
INT_MIN = -3**38

class Solution:

    def getLargestBSTSize(self, root, minValue, maxValue):

        if root is None:
            return True, INT_MAX, INT_MIN, 0 # because we compare the root's data with max of left and min of right and this makes it pass if its leaf


        isLeftBst, leftMin, leftMax, leftSize = self.getLargestBSTSize(root.left, minValue, maxValue)
        isRightBst, rightMin, rightMax, rightSize = self.getLargestBSTSize(root.right, minValue, maxValue)

        # process the node
        if isLeftBst and isRightBst and root.data > leftMax and root.data < rightMin:


            # for a leaf node
            if leftMin == INT_MAX:
                leftMin = root.data

            if rightMax == INT_MIN:
                rightMax = root.data

            return True, leftMin, rightMax, leftSize + 1 + rightSize

        else:
            return False, -1, -1, max(leftSize, rightSize)

    def largestBst(self, root):


        _, _, _, size = self.getLargestBSTSize(root, INT_MAX, INT_MIN)
        return size