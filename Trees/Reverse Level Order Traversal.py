"""
If we look at the output of reverse level order we will understand the patten.
If we do normal BFS/Level order just visit right subtree first and then left and reverse the overall ordering
we will have the expected output
"""


class Solution:
    def reverseLevelOrder(self, root):

        queue = [root]
        ordering = []

        while queue:

            curr = queue.pop(0)
            ordering.append(curr.data)

            if curr.right is not None:
                queue.append(curr.right)

            if curr.left is not None:
                queue.append(curr.left)

        return ordering[::-1]


