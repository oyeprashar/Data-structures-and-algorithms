class Solution:
    
    def height(self,root,ans):
    
        if root == None:
            return 0
            
        leftHeight = self.height(root.left,ans)
        rightHeight = self.height(root.right,ans)
        
        if abs(leftHeight-rightHeight) > 1:
            ans[0] = False
            
        return 1 + max(leftHeight,rightHeight)
    

    def isBalanced(self,root):
        
        ans = [True]
        self.height(root,ans)
        return ans[0]
