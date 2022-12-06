"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    
    def getPostorder(self,root,ordering):
        
        if root:
            for child in root.children:
                self.getPostorder(child,ordering)
            
            ordering.append(root.val)
    
    def postorder(self, root: 'Node') -> List[int]:
        
        ordering = []
        self.getPostorder(root,ordering)
        return ordering