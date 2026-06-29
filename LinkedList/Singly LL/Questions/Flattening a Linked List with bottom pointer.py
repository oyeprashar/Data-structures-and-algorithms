'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None


'''


class Solution:

    def merge(self,  root1, root2):

        # if we are done with one list, the bottom is everything of another list
        if root1 is None:
            return root2

        if root2 is None:
            return root1

        currNode = None

        if root1.data < root2.data:
            currNode = root1
            currNode.bottom = self.merge(root1.bottom, root2)
        else:
            currNode = root2
            currNode.bottom = self.merge(root1, root2.bottom)

        currNode.next = None
        return currNode

    # O(n*k)
    def flatten(self, root):

        if root is None or root.next is None:
            return root

        root.next = self.flatten(root.next)
        root = self.merge(root, root.next)
        return root
