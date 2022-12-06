# Searching a node in BinaryTree
#
# Use any traversing method to traverse the tree
# if current_node.data == key, print "YES" and break
# if traverse the whole tree and none of the node matches, print "NO"

class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def searchByKey(node,key):
    #first traversing the binary tree by level order traversal
    if node is None:
        return
    else:
        queue = []
        traversed_elements = []
        queue.append(node)

        while(len(queue)>0):
            curr = queue.pop(0)
            traversed_elements.append(curr.data)

            if curr.left is not None:
                queue.append(curr.left)
            if curr.right is not None:
                queue.append(curr.right)
        k = 0
        for item in traversed_elements:

            if item == key:

                k += 1


        if k >= 1:
            print("YES")
        else:
            print("NO")

        return


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

searchByKey(root,3)