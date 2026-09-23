"""
    - The most important thing is that e are not trying to create a balanced BST
    - We simply iterate the binary search tree till we find the leaf where we can insert the new node either in the
        left or right
"""



class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    # Function to insert a node in a BST.
    def insert(self, root, key):

        if root is None:
            return Node(key)

        if key < root.data:
            root.left = self.insert(root.left, key)

        elif key > root.data:
            root.right = self.insert(root.right, key)

        return root