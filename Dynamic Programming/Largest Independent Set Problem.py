class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None 
    
def maxLen(root,memory):

    if root == None:
        return 0 
    
    if root in memory:
        return memory[root]

    op1 = 1 
    if root.left != None:
        op1 += maxLen(root.left.left,memory)
        op1 += maxLen(root.left.right,memory)
    
    if root.right != None:
        op1 += maxLen(root.right.left,memory)
        op1 += maxLen(root.right.right,memory)
    
    op2 = maxLen(root.left,memory) + maxLen(root.right,memory) 
    
    memory[root] = max(op1,op2)
    return memory[root]

def getMaxLen(root):
    memory = {}
    return maxLen(root,memory)

root = Node(10)
root.left = Node(20)
root.left.left = Node(40)
root.left.right = Node(50)
root.left.right.left = Node(70)
root.left.right.right = Node(80)
root.right = Node(30)
root.right.right = Node(60)

print(getMaxLen(root))