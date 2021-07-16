from collections import defaultdict
class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def verticalOrder(root):
    hd = 0
    dict1 = defaultdict(list)
    dict2 = getverticalOrder(root,hd,dict1)
    result = []
    # we are first sorting the dictionary's keys
    # for key in sorted(dict2):
    #     result = result + dict2[key]  # all value lists are concatenated into a single list! IMPORTANT
    # return  result
    return dict2
def getverticalOrder(root,hd,dict1):
    # Base condition
    if root is None:
        return

    # this is kya karna h harr node parr
    dict1[hd].append(root.data)

    # this is ki left parr kya karna h aur right parr kya karna h
    getverticalOrder(root.left,hd-1,dict1)
    getverticalOrder(root.right,hd+1,dict1)

    return dict1

# root = BinaryTree(1)
# root.left = BinaryTree(2)
# root.right = BinaryTree(3)
# root.right.right = BinaryTree(6)
# root.left.left = BinaryTree(4)
# root.left.right = BinaryTree(5)

root = BinaryTree(2)
root.right = BinaryTree(3)
root.right.left = BinaryTree(4)

print(verticalOrder(root))

