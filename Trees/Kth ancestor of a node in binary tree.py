"""
Kth ancestor in binary tree
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getKthAncestorHelper(root, k, node, currPath, res):

    if root is None:
        return

    if root.data == node:
        ancestorIndex = len(currPath) - (k)
        if ancestorIndex >= 0 and ancestorIndex < len(currPath):
            res.append(currPath[ancestorIndex].data)
        return

    currPath.append(root)
    getKthAncestorHelper(root.left, k, node, currPath, res)
    getKthAncestorHelper(root.right, k, node, currPath, res)
    currPath.pop()



def getKthAncestor(root, k, node):
    currPath = []
    res = []
    getKthAncestorHelper(root, k, node, currPath, res)

    if len(res) == 0:
        return None

    return res[0]

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
print(getKthAncestor(root, 2, 5))




