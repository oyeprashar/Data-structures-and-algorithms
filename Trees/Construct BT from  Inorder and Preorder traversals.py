class Solution:

    def construct(self,left,right,currIndex,preorder,inorderDict):
        
        if left > right:
            
        currData = preorder[currIndex[0]]
        currIndex[0] += 1
        currNode = Node(currData)
        
        inorderIndex = inorderDict[currData]
        
        currNode.left = self.construct(left,inorderIndex-1,currIndex,preorder,inorderDict)
        currNode.right = self.construct(inorderIndex+1,right,currIndex,preorder,inorderDict)
        
        
        return currNode
        
    
    def buildtree(self, inorder, preorder, n):
        
        currIndex = [0]
        inorderDict = {}
        
        for index,value in enumerate(inorder):
            inorderDict[value] = index
            
        return self.construct(0,n-1,currIndex,preorder,inorderDict)    
