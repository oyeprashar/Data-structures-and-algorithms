prev = None
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printList(node):
    curr = node
    while(curr):
        print(curr.data)
        curr = curr.right

def BT2DLL(root):
    head = [0]
    BT2DLLHelper(root,head)
    return head[0]

def BT2DLLHelper(root,head):
    global prev  # making a variable global inside the scope of a function makes the variable static
    if root is None:
        return

    BT2DLLHelper(root.left,head)
    if prev is None:
        head[0] = root

    else:
        root.left = prev
        prev.right = root
    prev = root

    BT2DLLHelper(root.right,head)

root = BinaryTree(12)
root.left = BinaryTree(7)
root.left.left = BinaryTree(2)
root.left.right = BinaryTree(8)
root.right = BinaryTree(24)
head1 = BT2DLL(root)
printList(head1)

# printList(head1)
