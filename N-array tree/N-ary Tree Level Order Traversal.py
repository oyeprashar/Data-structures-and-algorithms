"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if root == None:
            return []
        
        ordering = []
        queue = [root]
        currLevel = [root.val]
        
        while len(queue) > 0:
            
            ordering.append(currLevel)
            currLevel = []
            
            # building the next level from parents sitting in the queue
            for _ in range(len(queue)):
                
                curr = queue.pop(0)
                
                if curr.children != None:
                    for child in curr.children:
                        
                        currLevel.append(child.val)
                        queue.append(child)
        return ordering