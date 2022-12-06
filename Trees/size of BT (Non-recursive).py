class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def sizeIterative(node):
    result = []
    queue = []
    queue.append(node)

    while(len(queue)>0):
        curr = queue.pop(0)
        result.append(curr.data)

        if curr.left is not None:
            queue.append(curr.left)

        if curr.right is not None:
            queue.append(curr.right)

    return len(result)

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

print(sizeIterative(root))