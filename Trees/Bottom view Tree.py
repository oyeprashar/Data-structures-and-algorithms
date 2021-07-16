class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def bottomView(root):
    hd = 0
    dict1 = {}
    result = []
    dict2 = getverticalOrder(root,hd,dict1)
    for key in sorted(dict2.keys()):
        items = dict2[key]
        result.append(items[-1])
        # if len(items) == 1:
        #     result.append(items[-1])
        # else:
        #     result.append(items[len(items)-2])
    return result
def getverticalOrder(root,hd,dict1):
    # Base condition
    if root is None:
        return

    # this is kya karna h harr node parr
    dict1.setdefault(hd,[])
    dict1[hd].append(root.data)

    # recursive calls to left and right children
    getverticalOrder(root.left,hd-1,dict1)
    getverticalOrder(root.right,hd+1,dict1)

    return dict1

# root = BinaryTree('a')
# root.left = BinaryTree('b')
# root.left.left = BinaryTree('d')
# root.left.right = BinaryTree('e')
# root.left.left.left = BinaryTree('h')
# root.left.left.right = BinaryTree('i')
# root.right = BinaryTree('c')
# root.right.left = BinaryTree('f')
# root.right.right = BinaryTree('g')
# root.right.right.left = BinaryTree('j')
# root.right.right.right = BinaryTree('k')


# GFG TEST CASE
# CURRENT O/P: [5, 10, 3, 22, 25]
# Expected O/P: 5  10  3  14  25
# Vertical Levels [[5], [8, 10], [20, 3], [14, 22], [25]]
root = BinaryTree(20)
root.left = BinaryTree(8)
root.left.left = BinaryTree(5)
root.left.right = BinaryTree(3)
root.left.right.left = BinaryTree(10)
root.left.right.right = BinaryTree(14)
root.right = BinaryTree(22)
root.right.right = BinaryTree(25)



print(bottomView(root))