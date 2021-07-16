class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def levelOrder(node_1):
    if node_1 is None:
        return
    queue = []
    queue.append(node_1)
    result = []

    while(len(queue)>0):
        curr = queue.pop(0)
        result.append(curr.data)

        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
    return result
def compareBTs(node1, node2):
    return levelOrder(node1) == levelOrder(node2)



root1 = BinaryTree(1)
root2 = BinaryTree(1)
root1.left = BinaryTree(2)
root1.right = BinaryTree(3)
root1.left.left = BinaryTree(4)
root1.left.right = BinaryTree(5)

root2.left = BinaryTree(2)
root2.right = BinaryTree(3)
root2.left.left = BinaryTree(4)
root2.left.right = BinaryTree(5)

print(compareBTs(root1,root2))
