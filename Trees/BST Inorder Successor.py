'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    
    def inOrderSuccessorHelper(self, root, k, res):
        
        if root is None:
            return None
            
        # if the value is greator, save it and minimise it
        if root.data > k.data:
            res[0] = root.data
            # move left to minmise this
            return self.inOrderSuccessorHelper(root.left, k, res)
        
        # move right if the value if equal or smaller to make it bigger
        else:
            return self.inOrderSuccessorHelper(root.right, k, res)
    
    def inOrderSuccessor(self, root, k):
        res = [-1]
        self.inOrderSuccessorHelper(root, k, res)
        return res[0]
        
