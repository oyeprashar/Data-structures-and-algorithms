# FINDING GREATEST ELEMENT IN BT WITHOUT RECURSION
# We will use level order traversion
# While deleting elements from queue we will compare and find the max

class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def MaxUsingLevelOrder(root):
    if root is None:
        return


    queue = []
    max_element = 0
    queue.append(root)
    while(len(queue)>0):
        node = queue.pop(0)

        if max_element < node.data:
            max_element = node.data

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)
    print(max_element)


root = BinaryTree(2)
root.left = BinaryTree(7)
root.right = BinaryTree(5)
root.left.right = BinaryTree(6)
root.left.right.left = BinaryTree(1)
root.left.right.right = BinaryTree(11)
root.right.right = BinaryTree(9)
root.right.right.left = BinaryTree(4)

MaxUsingLevelOrder(root)

