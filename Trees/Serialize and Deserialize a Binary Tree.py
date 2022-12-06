class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def deserialize(queue1):
    if len(queue1) > 0:  # agar queue empty nhi hai tabhi hum pop karengye
        node = BinaryTree(queue1.pop(0))
    if node.data == 'X':  # agar 'X' encounter kiya hai humne toh kuch mat kro
        return
    else:
        node.left = deserialize(queue1) # recursively saare elements ka left aur right bna te jayengye
        node.right = deserialize(queue1)
    return node  # recursion me starting me jo node diya tha wahi return hoga because problem is divided into sub-problem and then the main problem is solved and returned


def serialize(root):
    result = []
    inorder(root, result)
    return result


def inorder(root, result):
    if root is None:
        result.append('X')  # for example agar ek node hai 2 with no children aisa likha hoga -> 2,X,X
        return
    else:
        result.append(root.data)
        inorder(root.left, result)
        inorder(root.right, result)


root = BinaryTree(1)
root.left = BinaryTree(2)
root.left.left = BinaryTree(3)
root.left.right = BinaryTree(4)
root.right = BinaryTree(5)

serialized_list = serialize(root)
print(serialized_list)
n1 = deserialize(serialized_list)
print(n1.data)
print(n1.left.data)
print(n1.left.left.data)
print(n1.left.right.data)

print(n1.right.data)


