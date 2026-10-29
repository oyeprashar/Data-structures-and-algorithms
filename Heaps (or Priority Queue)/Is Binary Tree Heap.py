"""
What is seenNone doing?
    - The nodes in a heap are filled from left to right
    - None nodes are allow in the lowest left at the right most side
    - That simply means that once we encounter a None node, we should not see another non-none node
"""

class Solution:

    def isPropertyVoilated(self, node):

        if node.left is None and node.right is not None:
            return True

        if node.left is not None and node.data < node.left.data:
            return True

        if node.right is not None and node.data < node.right.data:
            return True

        return False

    def isHeap(self, root):

        queue = [root]
        seenNone = False

        while queue:

            curr = queue.pop(0)

            if self.isPropertyVoilated(curr):
                return False

            if curr.left is not None:

                if seenNone:
                    return False

                queue.append(curr.left)

            if curr.right is not None:

                if seenNone:
                    return False

                queue.append(curr.right)

            if curr.left is None or curr.right is None:
                seenNone = True

        return True
