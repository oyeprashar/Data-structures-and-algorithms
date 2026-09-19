
class Solution:

    def checkSumTree(self, root, currLevel, lastLeafLevel, res):

        if root is None:
            return

        if root.left is None and root.right is None:

            if lastLeafLevel[0] == -1:
                lastLeafLevel[0] = currLevel

            elif currLevel != lastLeafLevel[0]:
                res[0] = False


        self.checkSumTree(root.left, currLevel + 1, lastLeafLevel, res)
        self.checkSumTree(root.right, currLevel + 1, lastLeafLevel, res)

    def check(self, root):


        res = [True]
        lastLeafLevel = [-1]
        self.checkSumTree(root, 0, lastLeafLevel, res)
        return res[0]

