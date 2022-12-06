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

    res = [-3**38] 
    maxPathSumUtil(root, res) 
    return res[0]             

def maxPathSumUtil(root, res):


    if root == None:
        return None

    if root.left == None and root.right == None:
        return root.data

    leftAns = maxPathSumUtil(root.left,res)
    rightAns = maxPathSumUtil(root.right,res)

    if leftAns != None and rightAns != None:
        res[0] = max(res[0],root.data + leftAns + rightAns)
        return root.data + max(leftAns,rightAns)

    if leftAns != None:
        return root.data + leftAns

    if rightAns != None:
        return root.data + rightAns





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