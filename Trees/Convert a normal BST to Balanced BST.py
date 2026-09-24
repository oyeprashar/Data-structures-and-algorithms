
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None



class Solution:

    def generateInorder(self, root, arr):
        if root is None:
            return

        self.generateInorder(root.left, arr)
        arr.append(root.data)
        self.generateInorder(root.right, arr)

    def generateBST(self, left, right, arr):

        if left > right:
            return None

        mid = (left + right) // 2
        currNode = Node(arr[mid])
        currNode.left = self.generateBST(left, mid - 1, arr)
        currNode.right = self.generateBST(mid + 1, right, arr)

        return currNode

    def balanceBST(self, root):
        arr = []
        self.generateInorder(root, arr)
        return self.generateBST(0, len(arr) - 1, arr)
