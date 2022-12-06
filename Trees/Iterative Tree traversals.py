 class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def iterativeTraversals(root):
    
    if root == None:
        return "NO TREE AVAILABLE AT THIS ROOT"

    stack = [[root,1]]

    preorder = ""
    inorder = ""
    postorder = ""

    while len(stack) > 0:

        top = stack[-1]

        if top[1] == 1:
            preorder += str(top[0].data)
            top[1] += 1

            if top[0].left != None:
                stack.append([top[0].left,1])

        elif top[1] == 2:
            inorder += str(top[0].data)
            top[1] += 1

            if top[0].right != None:
                stack.append([top[0].right,1])

        else:
            top = stack.pop()
            postorder += str(top[0].data)


    print("preorder :",preorder,"inorder :",inorder,"postorder :",postorder)



root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)

iterativeTraversals(root)


