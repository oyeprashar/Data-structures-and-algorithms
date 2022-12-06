"""
A binary tree and a number k are given. 
Print every path in the tree with sum of the nodes in the path as k. 
A path can start from any node and end at any node and must be downward only,
i.e. they need not be root node and leaf node; and negative numbers can also be there in the tree.
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def findPaths(root,currPath,ans,k):

    if root == None:
        return 

    currPath.append(root.data)
    findPaths(root.left,currPath,ans,k)
    findPaths(root.right,currPath,ans,k)
    
    curr = []
    currSum = 0
    index = len(currPath)-1

    while index >= 0:

        curr.append(currPath[index])
        currSum += currPath[index]

        if currSum == k:
            ans.append(curr[::-1])

        index -= 1

    currPath.pop()

def getPaths(root,k):

    ans = []

    findPaths(root,[],ans,k)

    return ans

   

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
root.right.right.right = Node(6)

print(getPaths(root,5))