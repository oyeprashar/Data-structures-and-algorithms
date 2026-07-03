
"""
duplicate subtree of size two or more.
"""

class Solution:

    def duplicateSubTree(self, root, freq):
        ### The subtree should be size two of more! That means single nodes should not be in the freq dic

        # null nodes! Return some placeholder
        if root is None:
            return "X"

        # return the leaf nodes to make sure the dict contains trees of sizes > 1 i.e. size >= 2
        if root.left is None and root.right is None:
            return str(root.data)

        leftPart = self.duplicateSubTree(root.left, freq)
        rightPart = self.duplicateSubTree(root.right, freq)

        # Since we returned for leaf nodes, the currSubtree is always > 1 i.e. >= 2
        currSubtree = "(" + leftPart + ")" + str(root.data) + "(" + rightPart + ")"

        if currSubtree in freq:
            freq[currSubtree] += 1
        else:
            freq[currSubtree] = 1

        return currSubtree


    def dupSub(self, root):

        freq = {}
        self.duplicateSubTree(root, freq)

        for key in freq:
            if freq[key] > 1:
                return True
        return False

