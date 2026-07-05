"""
- Print every path in the tree with sum of the nodes in the path as k.
- A path can start from any node and end at any node and must be downward only
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pathWithSumKHelper(root, k, currPath):

    if root is None:
        return None

    # Add the node to the current path and check moving upwards
    # This makes sure all the paths are considered moving upwards
    currPath.append(root.data)
    currSum = 0
    currNodes = []
    for i in range(len(currPath)-1,-1,-1):

        currNodes.append(currPath[i])
        currSum += currPath[i]

        if currSum == k:
            print(currNodes[::-1]) # since we want to add the nodes downwards but the loop was down to up

    # go left and right
    pathWithSumKHelper(root.left, k, currPath)
    pathWithSumKHelper(root.right, k, currPath)

    # remove the node from the current path
    currPath.pop()


def pathWithSumK(root, k):
    pathWithSumKHelper(root, k, [])

# Test code
root = Node(1)
root.left = Node(3)
root.left.left = Node(2)
root.left.right = Node(1)
root.left.right.left = Node(1)
root.right = Node(-1)
root.right.left = Node(4)
root.right.left.left = Node(1)
root.right.left.right = Node(2)
root.right.right = Node(5)
root.right.right.right = Node(2)
pathWithSumK(root, 5)
