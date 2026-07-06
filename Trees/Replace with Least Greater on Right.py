"""
The question is asking for the least greator value on the rigth and not the greatest value! That makes it trickier.

Approach
 - Traverse the array from right to left
 - Find the inorder success of the current value, write it in the ans array
 - Insert the current number into the BST
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:

    def insertIntoBST(self, root, newData):

        if root is None:
            return Node(newData)

        if root.data > newData:
            root.left = self.insertIntoBST(root.left, newData)

        else:
            root.right = self.insertIntoBST(root.right, newData)

        return root

    def findInorderSuccessor(self, root, targetValue, res):

        if root is None:
            return None

        if root.data > targetValue:
            res[0] = root.data
            return self.findInorderSuccessor(root.left, targetValue, res)

        else:
            return self.findInorderSuccessor(root.right, targetValue, res)

    def findLeastGreater(self, arr):

        root = Node(arr[-1])
        ans = [-1] * len(arr)

        for i in range(len(arr) - 2, -1, -1):
            res = [-1]
            self.findInorderSuccessor(root, arr[i], res)
            ans[i] = res[0]
            self.insertIntoBST(root, arr[i])

        return ans
