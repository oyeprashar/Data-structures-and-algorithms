INT_MAX = 3**38

class Solution:
    def checking(self,root,level,lastLevel):
        
        if root == None:
            return True
    
        if root.left == None and root.right == None:
            if lastLevel[0] == INT_MAX:
                lastLevel[0] = level
                return True
            
            elif lastLevel[0] != level:
                return False
                
        return self.checking(root.left,level+1,lastLevel) and self.checking(root.right,level+1,lastLevel)
            
    def check(self, root):
        lastLevel = [INT_MAX]
        return self.checking(root,1,lastLevel)

        