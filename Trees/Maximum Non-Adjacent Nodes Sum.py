"""
Time complexity :
    - Without memoisation : O(2^n) because there are two options at every node
    - With memoisation : O(n)
"""
class Solution:


    def getMaxSumHelper(self, root, cache):

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return root.data

        if root in cache:
            return cache[root]

        op1 = root.data

        if root.left is not None:
            op1 += self.getMaxSumHelper(root.left.left, cache)
            op1 += self.getMaxSumHelper(root.left.right, cache)

        if root.right is not None:
            op1 += self.getMaxSumHelper(root.right.left, cache)
            op1 += self.getMaxSumHelper(root.right.right, cache)

        op2 = self.getMaxSumHelper(root.left, cache) + self.getMaxSumHelper(root.right, cache)

        return max(op1, op2)

    def getMaxSum(self, root):
        cache = {}
        return getMaxSumHelper(root, cache)
