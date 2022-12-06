class Solution:
    def leftSide(self,root,leftArr):
        
        if root == None or root.left == None and root.right == None:
            return 
        
    
        leftArr.append(root.data)
        
        if root.left != None:
            self.leftSide(root.left,leftArr)
        
        elif root.right != None:
            self.leftSide(root.right,leftArr)
            
    def rightSide(self,root,rightArr):
        
        if root == None or root.left == None and root.right == None:
            return 
        
        rightArr.append(root.data)
        
        if root.right != None:
            self.rightSide(root.right,rightArr)
            
        elif root.left != None:
            self.rightSide(root.left,rightArr)
            
    def leafNodes(self,root,leafArr):
        
        if root == None:
            return 
        
        if root.left == None and root.right == None:
            leafArr.append(root.data)
        
        self.leafNodes(root.left,leafArr)
        self.leafNodes(root.right,leafArr)
            
    
    def printBoundaryView(self, root):
        if root == None:
            return []
            
        leftArr = []
        self.leftSide(root.left,leftArr)
        
        rightArr = []
        self.rightSide(root.right,rightArr)
        
        leafArr = []
        self.leafNodes(root,leafArr)
        
        ans = [root.data]
        
        ans.extend(leftArr)
        ans.extend(leafArr)
        ans.extend(rightArr[::-1])
        
        return ans
            