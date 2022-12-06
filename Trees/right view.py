class Solution:
    def getRightView(self,root,currLevel,lastLevel,ans):
        
        if root == None:
            return 
    
        if currLevel > lastLevel[0]:
            lastLevel[0] = currLevel
            ans.append(root.data)
        
        self.getRightView(root.right,currLevel+1,lastLevel,ans)            
        self.getRightView(root.left,currLevel+1,lastLevel,ans)            
            
        
        
    def rightView(self,root):
        
        if root == None:
            return []
        
        lastLevel = [0]
        ans = []
        
        self.getRightView(root,1,lastLevel,ans)            
        
        return ans