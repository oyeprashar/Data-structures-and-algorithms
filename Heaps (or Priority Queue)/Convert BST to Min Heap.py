"""
Convert a BST into Min Heap

Approach :
    1. We find the sorted array when we do inorder traversal of the BST
    3. Now we want to overwrite the data s.t the parent is smaller than children (min heap)
       This can be done if we overwrite the original BST with inorder data in preorder, this ensures that we are using
       the smaller elements first and the parent will be smaller than the child. Smallest at the root of the tree.

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root, arr):

    if root:
        inorder(root.left, arr)
        arr.append(root.data)
        inorder(root.right, arr)

def createHeap(currIndex, inorderArr, root):

    if currIndex[0] == len(inorderArr) or root is None:
        return None

    root.data = inorderArr[currIndex[0]]
    currIndex[0] += 1
    createHeap(currIndex, inorderArr, root.left)
    createHeap(currIndex, inorderArr, root.right)


def convertBSTtoMinHeap(root):
    inorderArr = []
    inorder(root, inorderArr)
    currIndex = [0]
    createHeap(currIndex, inorderArr, root)
    return root




