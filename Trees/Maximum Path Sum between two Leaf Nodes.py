#====MAXIMUM PATH SUM BETWEEN TWO LEAF NODES LOGIC====
# If node is None then don't do anything just return
# if node is a leaf node then return its data
# if node is not a leaf then update the max sum and return max(l,r)+node.data
# IMPORTANT: since we are passing a list(or array) to the function, the list is updated in the real time i.e. the actual
#            list is updated that we passed to the function.
class BinaryTree():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxPathSum(root):

    INT_MIN = - 2**32
    res = [INT_MIN] # this is a list
    maxPathSumUtil(root, res) # IMP: since a list is passed to this function, the updation happens in realtime
    return res[0]             # hence we can directly return the list instead!!

def maxPathSumUtil(root, res):


    if root is None:
        return

    if root.left is None and root.right is None:
        return root.data

    ls = maxPathSumUtil(root.left, res)
    rs = maxPathSumUtil(root.right, res)

    if root.left is not None and root.right is not None:

        res[0] = max(res[0], ls + rs + root.data)

        return max(ls,rs) + root.data

    if root.left is None:
        return rs + root.data
    else:
        return ls + root.data



root = BinaryTree(-15)
root.left = BinaryTree(5)
root.right = BinaryTree(6)
root.left.left = BinaryTree(-8)
root.left.right = BinaryTree(1)
root.left.left.left = BinaryTree(2)
root.left.left.right = BinaryTree(6)
root.right.left = BinaryTree(3)
root.right.right = BinaryTree(9)
root.right.right.right= BinaryTree(0)
root.right.right.right.left = BinaryTree(4)
root.right.right.right.right = BinaryTree(-1)
root.right.right.right.right.left = BinaryTree(10)

print(maxPathSum(root))