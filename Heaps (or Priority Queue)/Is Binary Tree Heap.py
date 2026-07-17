"""
Approach :
    We do can check this with one pass of BFS/Level Order Traversal
        1. Completeness : Once we encounter a non node, all the nodes after this needs to be None and if we find a
            non-none after a none node then the tree is not complete
        2. Max Heap property : parent.data >= parent.left.data and parent.data >= parent.right.data
"""

class Solution:

    def isHeap(self, root):
        
        seenNone = False
        queue = [root]

        while len(queue) > 0:

            curr = queue.pop(0)
            
            if curr.left is None:
                seenNone = True

            else:
                if seenNone or curr.left.data > curr.data:
                    return False
                
                queue.append(curr.left)

            if curr.right is None:
                seenNone = True

            else:
                if seenNone or curr.right.data > curr.data:
                    return False

                queue.append(curr.right)

        return True
