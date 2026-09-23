# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def findSmallestNode(self, root):

        curr = root
        while curr.left is not None:
            curr = curr.left

        return curr

    def deleteNode(self, root, key):

        if root is None:
            return None

        if key < root.data:
            root.left = self.deleteNode(root.left, key)

        elif key > root.data:
            root.right = self.deleteNode(root.right, key)


        ###### Deletion logic goes here
        else:

            if root.left is None and root.right is None:
                return None

            if root.left is None and root.right is not None:
                return root.right

            if root.right is None and root.left is not None:
                return root.left

            smallestRightNode = self.findSmallestNode(root.right)
            root.data = smallestRightNode.data
            root.right = self.deleteNode(root.right, smallestRightNode.data)

        return root



