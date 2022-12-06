
"""
Input :       1
            /    \
          -2      3
          / \    /  \
         4   5  -6   2
"""
class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def largestSum(root,ans):

    if root == None:
        return 0

    if root.left == None and root.right == None:
        return root.data

    leftSum = largestSum(root.left,ans)
    rightSum = largestSum(root.right,ans)

    currSum = root.data + leftSum + rightSum

    ans[0] = max(ans[0],currSum)

    return currSum

def getLargestSum(root):
    ans = [-3**38]
    largestSum(root,ans)
    return ans[0]



root = Node(1)
root.left = Node(-2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(-6)
root.right.right = Node(2)

print(getLargestSum(root))

root2 = Node(1)
root2.left = Node(2)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right = Node(3)
root2.right.left = Node(6)
root2.right.right = Node(7)

print(getLargestSum(root2))

