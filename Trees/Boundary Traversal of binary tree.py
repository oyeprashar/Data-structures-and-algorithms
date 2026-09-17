"""
A very important note : <------ EXTREMELY IMPORTANT
    In this problem, the left side answer is not left view. Because in left view, it is literally how the tree would look
    if we saw it from the left

    The left answer is the left boundary, a continuous left path.

    The same logic applies to the right path
"""




class Solution:

    def getLeftBoundary(self, root, currLevel, lastLevel, leftBoundary):

        if root is None or (root.left is None and root.right is None):
            return

        if currLevel > lastLevel[0]:
            leftBoundary.append(root.data)
            lastLevel[0] = currLevel

        # We do this because we want to trace the left boundary
        if root.left is not None:
            self.getLeftBoundary(root.left, currLevel + 1, lastLevel, leftBoundary)
        else:
            self.getLeftBoundary(root.right, currLevel + 1, lastLevel, leftBoundary)

    def getRightBoundary(self, root, currLevel, lastLevel, rightBoundary):

        if root is None or (root.left is None and root.right is None):
            return

        if currLevel > lastLevel[0]:
            rightBoundary.append(root.data)
            lastLevel[0] = currLevel

        # We do this because we want to trace the right boundary
        if root.right is not None:
            self.getRightBoundary(root.right, currLevel + 1, lastLevel, rightBoundary)

        else:
            self.getRightBoundary(root.left, currLevel + 1, lastLevel, rightBoundary)

    def getLeaves(self, root, leaves):

        if root is None:
            return

        if root.left is None and root.right is None:
            leaves.append(root.data)
            return

        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)

    def boundaryTraversal(self, root):

        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.data]

        leftBoundary = []
        rightBoundary = []
        leaves = []

        self.getLeftBoundary(root.left, 0, [-1], leftBoundary)
        self.getRightBoundary(root.right, 0, [-1], rightBoundary)
        self.getLeaves(root, leaves)

        # rightBoundary.pop(0)

        res = []
        res.append(root.data)
        res.extend(leftBoundary)

        res.extend(leaves)
        res.extend(rightBoundary[::-1])

        return res
