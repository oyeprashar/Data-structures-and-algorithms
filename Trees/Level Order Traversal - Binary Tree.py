# LOGIC FOR LEVEL ORDER TRAVERSAL
#   Create a queue
#   1) Append the root node to queue
#   2) pop and print this root node
#   3) Append left and right child of this root node top the queue
#   4) Repeat until the queue is empty

class BinaryTree():
    # initializing
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return

    queue = []

    queue.append(root)
    result = []
    while(len(queue) >0):


        result.append(queue[0].data)
        node = queue.pop(0)

        if node.left is not None:
            queue.append(node.left)

        if node.left is not None:
            queue.append(node.right)
    return result
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

print("Level Order Traversal of binary tree is -")
print(printLevelOrder(root))