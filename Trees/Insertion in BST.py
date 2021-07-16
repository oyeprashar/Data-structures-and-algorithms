class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insert(root,key):
    if root is None:    # if no bst exists on the given root
        return BST(key)

    if root.data == key: # if node with same value already exists, return that node
        return root

    if root.data < key:
        if root.right is None:
            root.right = BST(key)

        else:
            insert(root.right,key) # else recursively go right and check all conditions again
    else:
        if root.left is None:
            root.left = BST(key)

        else:
            insert(root.left,key)  # else recursively go left and check all conditions again
    return root  # call stack me in the end orignal root hi nikalega jisse call kiya tha (make the call stack is not getting this)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

r = BST(50)
r = insert(r, 30)  # we are saying r = insert() because insert function is returning the root of the new BST
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
inorder(r)