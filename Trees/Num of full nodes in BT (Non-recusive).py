class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def numofFullNodes(node):
    if node is None:
        return 0

    queue = []
    queue.append(node)
    count = 0
    while(len(queue)>0):
        curr = queue.pop(0)
        # bass ek extra if statement ki both are not None
        if curr.left is not None and curr.right is not None:
            count  += 1

        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
                queue.append(curr.right)
    return count

root = BinaryTree(2)
root.left = BinaryTree(7)
root.right = BinaryTree(5)
root.left.right = BinaryTree(6)
root.left.right.left = BinaryTree(1)
root.left.right.right = BinaryTree(11)
root.right.right = BinaryTree(9)
root.right.right.left = BinaryTree(4)

print(numofFullNodes(root))