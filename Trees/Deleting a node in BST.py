
class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


def minVal(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root,node):

    if root is None:
        return root  

    if node.data < root.data:                   # we are assigning this as root.left to know the parent jisske baad delete hona h
        root.left = deleteNode(root.left,node)  # maanlo RHS of this find the node to be deleted, deletes it and returns None, the parent's left is None
                                                # and that's what we wanted.
    elif node.data > root.data:
        root.right = deleteNode(root.right,node)

    # if node.data matches with the current node
    else:
        if root.left is None:                  # also note that this case also covers the case where a node is leaf
            temp = root.right                  # simply the node is changed to None
            root = None                        # since its right is None, None is returned and parent now points to None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # if the node to be deleted has a left and right child
        # we replace it with inorder successor (min node in right)  and
        # delete the inorder successor

        temp = minVal(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right,temp)
        return root
        
    return root

root = BST(50)
root.left = BST(30)
root.left.left = BST(20)
root.left.right = BST(40)
root.right = BST(70)
root.right.left = BST(60)
root.right.right = BST(80)

print("====INORDER-BEFORE-DELETION====")
inorder(root)
root = deleteNode(root,root.left.left)
print("====INORDER-AFTER-DELETING-20====")
inorder(root)
root = deleteNode(root,root.left)
print("====INORDER-AFTER-DELETING-30====")
inorder(root)