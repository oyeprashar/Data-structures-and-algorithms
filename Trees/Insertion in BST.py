class Node:

    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 

def insert(root,key):

    if root == None:
        return Node(key)

    elif key < root.data:

        if root.left == None:
            root.left = Node(key)

        else:
            insert(root.left,key)

    elif key > root.data:

        if root.right == None:
            root.right = Node(key)

        else:
            insert(root.right,key)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

r = Node(50)
insert(r, 30)  # we are saying r = insert() because insert function is returning the root of the new BST
insert(r, 20)
insert(r, 40)
insert(r, 70)
insert(r, 60)
insert(r, 80)
inorder(r)