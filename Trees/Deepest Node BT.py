# FINDING DEEPEST ELEMENT IN BT
# LOGIC -> The last element in level order traversal is always the deepest element
class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def deepestNode(node):
    # using level order traversal

    queue = []
    queue.append(node)
    while(len(queue)>0):
        curr = queue.pop(0)
        if curr.left is not None:
            queue.append(curr.left)

        if curr.right is not None:
            queue.append(curr.right)
    return curr.data

root = BinaryTree(2)
root.left = BinaryTree(7)
root.right = BinaryTree(5)
root.left.right = BinaryTree(6)
root.left.right.left = BinaryTree(1)
root.left.right.right = BinaryTree(11)
root.right.right = BinaryTree(9)
root.right.right.left = BinaryTree(4)

print(deepestNode(root))