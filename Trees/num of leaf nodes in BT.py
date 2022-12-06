# FINDING NUMBER OF LEAF NODES (NO CHILDREN)
# LOGIC:
# We are using level order traversing and whenever we find a node with no left AND right child we increment count by 1
class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def numOfLeaf(node):
    if node is None:
        return 0
    queue = []
    queue.append(node)
    count = 0

    while(len(queue)>0):
        node = queue.pop(0)

        # Bass ek extra if satement ki both are None
        if node.left is None and node.right is None:
            count += 1

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

    return count
root = BinaryTree(2)
root.left = BinaryTree(7)
root.right = BinaryTree(5)
root.left.right = BinaryTree(6)
root.left.right.left = BinaryTree(1)
root.left.right.right = BinaryTree(11)
root.right.right = BinaryTree(9)
root.right.right.left = BinaryTree(4)

print(numOfLeaf(root))