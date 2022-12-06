class Solution:
    
    def findLCA(self,root,a,b):
        
        if root == None:
            return None
        
        if root.data == a or root.data == b:
            return root
        
        leftAns = self.findLCA(root.left,a,b)
        rightAns = self.findLCA(root.right,a,b)
        
        if leftAns != None and rightAns != None:
            return root
        
        if leftAns == None and rightAns == None:
            return None
        
        if leftAns != None:
            return leftAns
        
        if rightAns != None:
            return rightAns
            
    def findDistFromLCA(self,root,key,dist):
        
        if root == None:
            return 0
        
        if root.data == key:
            return dist
        
        return self.findDistFromLCA(root.left,key,dist+1) + self.findDistFromLCA(root.right,key,dist+1)
        
    
    def findDist(self,root,a,b):
        
        LCA = self.findLCA(root,a,b)
        dist1 = self.findDistFromLCA(LCA,a,0)
        dist2 = self.findDistFromLCA(LCA,b,0)
        
        return (dist1+dist2) 