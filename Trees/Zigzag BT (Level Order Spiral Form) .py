# ZIG ZAG -> Link to post: https://www.geeksforgeeks.org/level-order-traversal-in-spiral-form/
# LOGIC:
# getLevel returns a dictionary with key as level and its value are nodes at that level
# zigzag function reverses the nodes at odd level and even level remains the same
# zigzag converts list of list into single list using two nested loops
# at last zigzag converts the final list into a string and returns it
from collections import defaultdict
class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def getLevel(root,dict1,level):
    if root is None:
        return

    dict1[level].append(root.data)

    getLevel(root.left,dict1,level+1)
    getLevel(root.right,dict1,level+1)

    return dict1

def zigzag(root,dict1,level):
    dict1 = defaultdict(list)
    dict2 = getLevel(root,dict1,level)

    result = []
    for key in dict2:
        if key % 2 == 0:    # even levels are printed normally
            result.append(dict2[key])
        else:
            ans = dict2[key]        # odd levels are reversed
            result.append(ans[::-1])
    final = []
    for listitem in result:
        for item in listitem:
            final.append(str(item))
    string1 = " ".join(final)
    print(string1)


dict1 = {}
level = 0
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(7)
root.left.right = BinaryTree(6)
root.right.left = BinaryTree(5)
root.right.right = BinaryTree(4)


zigzag(root,dict1,level)
