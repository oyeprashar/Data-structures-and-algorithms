"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def getPreorder(self,root,ordering):
        
        if root:  
            ordering.append(root.val)
            for child in root.children:
                self.getPreorder(child,ordering)
        
    def preorder(self, root: 'Node') -> List[int]:
        ordering = []
        self.getPreorder(root,ordering)
        return ordering