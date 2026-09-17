"""
The left view is literally the left side of the binary tree. The first node on each level when we traverse down the tree
in (left, right) motion

"""


class Solution:

    def getLeftView(self, root, currLevel, lastLevel, res):

        if root is None:
            return

        if currLevel > lastLevel[0]:
            res.append(root.data)
            lastLevel[0] = currLevel

        self.getLeftView(root.left, currLevel + 1, lastLevel, res)
        self.getLeftView(root.right, currLevel + 1, lastLevel, res)



    def leftView(self, root):

        lastLevel = [-1]
        res = []
        self.getLeftView(root, 0, lastLevel, res)
        return res
