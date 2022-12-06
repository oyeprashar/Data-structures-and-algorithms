class Solution:
    
    def flatten(self, root: Optional[TreeNode]) -> None:
        
        if root == None:
            return 
        
        leftNode = root.left
        rightNode = root.right
        
        self.flatten(root.left)
        self.flatten(root.right)
    
        root.left = None
        root.right = leftNode
        
        end = root
        while end.right != None:
            end = end.right
        
        end.right = rightNode
        