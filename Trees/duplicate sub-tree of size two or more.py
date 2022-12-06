class Solution:
    def duplicate_checker(self,root,dict1):
        if root == None:
            return "$"
        
        if root.left == None and root.right == None:
            return str(root.data)
        
        leftStr = self.duplicate_checker(root.left,dict1)
        rightStr = self.duplicate_checker(root.right,dict1)
        
        currStr = leftStr + str(root.data) + rightStr
        
        if currStr in dict1:
            dict1[currStr] += 1
        else:
            dict1[currStr] = 1
        
        return currStr
        
    def dupSub(self, root):
        
        dict1 = {}
        self.duplicate_checker(root,dict1)
        
        for item in dict1:
            if dict1[item] > 1:
                return 1
            
        return 0