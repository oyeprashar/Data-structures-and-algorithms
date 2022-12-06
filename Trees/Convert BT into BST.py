class Solution:
    
    # this uses inorder traversal
    
    def BT2Array(self,root,arr):
        
        if root != None:
            self.BT2Array(root.left,arr)
            arr.append(root.data)
            self.BT2Array(root.right,arr)
            
    def convertArr2BST(self,root,arr):
        
        if root != None:
            self.convertArr2BST(root.left,arr)
            
            currD = arr.pop(0)
            root.data = currD
          
            self.convertArr2BST(root.right,arr)
        
        
    def binaryTreeToBST(self, root):
        
        if root == None:
            return root
        
        arr = []
        self.BT2Array(root,arr)
        
        arr.sort()

        self.convertArr2BST(root,arr)
        
        return root
        