"""
Important update :
    In GFG, earlier they wanted us to return the number of nodes but now they want then number of edges.

    Counting the edges in the diameter :
        - Our height code is still counting the number of nodes
        - When we check the diameter, we wont do +1 to it and this will make sure we are counting the edges and not nodes
"""





class Solution:

    def getDiameter(self, root, res):
        if root is None:
            return 0

        leftHeight = self.getDiameter(root.left, res)
        rightHeight = self.getDiameter(root.right, res)
        res[0] = max(res[0], leftHeight + rightHeight)

        return 1 + max(leftHeight, rightHeight)

    def diameter(self, root):
        res = [-3 ** 38]
        self.getDiameter(root, res)
        return res[0]
