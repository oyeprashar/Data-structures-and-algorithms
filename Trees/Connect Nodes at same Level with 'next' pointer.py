# TIME COMPLEXITY : O(N) | SPACE COMPLEXITY = O(1)
# // to understand read the notes in volume II

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        curr = root
        
        while curr != None:
            
            dummy = Node(0)
            temp = dummy
            
            while curr != None:
                
                if curr.left != None:
                    temp.next = curr.left 
                    temp = temp.next
                
                if curr.right != None:
                    temp.next = curr.right
                    temp = temp.next
                
                curr = curr.next
            
            curr = dummy.next
        
        return root
                
                


"""
CONNECTING NODES AT THE SAME LEVEL
# LOGIC
# Outer while loop will work until the queue is empty --> Like normal level order traversal
# Inner for loop runs jitne bhi element hongye at the same level, it is used to pop elements
#   at the same level and connect them, as they are popped and hence elements at same level are
#   removed from the queue as well and there children are appended
# child of curr is appended to queue like we do in normal level order traversal
IMPORTANT: prev is set to None before beginning of each level
"""
class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None

def connectNodes(root):

    queue = []
    queue.append(root)

    while(len(queue)>0):
        size = len(queue)
        prev = None                     # IMPORTANT: prev is set to None before beginning of each level

        for _ in range(size):           # we are running this loop so that we can pop the nodes at same levels
            curr = queue.pop(0)         # we pop the nodes at same leve and connect them

            if prev != None:
                prev.next = curr
            prev = curr

            if curr is not None:
                if curr.left is not None:
                    queue.append(curr.left)
                if curr.right is not None:
                    queue.append(curr.right)




root = BinaryTree(10)
root.left = BinaryTree(8)
root.right = BinaryTree(2)
root.left.left = BinaryTree(3)
root.right.right = BinaryTree(44)
connectNodes(root)
print(root.left.next.data)
print(root.left.left.next.data)
print(root.right.next)
print(root.right.right.next)
