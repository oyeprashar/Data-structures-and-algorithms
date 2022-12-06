INT_MAX = 3**38
INT_MIN = -3**38

class Solution:
    
    def largestBstHelper(self,root,max1,min1):
        
        if root == None:
            return 1,0,INT_MIN,INT_MAX
        
        if root.right == None and root.left == None:
            return 1,1,root.data,root.data
        
        isLeftBST,leftSize,leftMax,leftMin = self.largestBstHelper(root.left,max1,min1)
        isRightBST,rightSize,rightMax,rightMin = self.largestBstHelper(root.right,max1,min1)
        
        
        if isLeftBST == 1 and isRightBST == 1 and root.data > leftMax and root.data < rightMin:
            if leftMin == INT_MAX:
                leftMin = root.data
            
            if rightMax == INT_MIN:
                rightMax = root.data
            
            
            return 1,leftSize+1+rightSize,rightMax,leftMin
        
        else:
            return 0,max(leftSize,rightSize),0,0
            
    
    
    def largestBst(self, root):
        if root == None:
            return 1
        
        isBST,size1,max1,min1 = self.largestBstHelper(root,INT_MAX,INT_MIN)
        
        return size1