"""
Time complexity : O(n)
Space complexity : O(n)
"""
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
    
        queue = [(root,1)]
        ans = 0
        
        while len(queue) != 0:
            
            ans = max(ans,queue[-1][1]-queue[0][1]+1)
            size = len(queue)
            
            for _ in range(size):
                
                currTuple = queue.pop(0)
                currNode = currTuple[0]
                currIndex = currTuple[1]
                
                if currNode.left != None:
                    queue.append((currNode.left,2*currIndex))
                
                if currNode.right != None:
                    queue.append((currNode.right,2*currIndex+1))
                
        return ans
