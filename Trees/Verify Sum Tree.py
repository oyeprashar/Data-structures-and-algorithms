"""
In sum tree following properties are obeyed
    1. Root.data = leftRes + rightRes
    2. subtree returns : leftRes + root.data + rightRes to its parent

We need to do this while keeping track that the property is obeyed at each node
"""

class Solution:


    def checkSumTree(self, root, ans):

        if root is None:
            return 0

        if root.left is None and root.right == None:
            return root.data

        leftRes = self.checkSumTree(root.left, ans)
        rightRes = self.checkSumTree(root.right, ans)

        if root.data != leftRes + rightRes:
            ans[0] = False

        return leftRes + root.data + rightRes


    def is_sum_tree(self, node):

        ans = [True]
        self.checkSumTree(root, ans)
        return ans[0]
