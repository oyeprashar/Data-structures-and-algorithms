class Solution:
    
    def findMaxSum(self,root,memory):
        
        if root == None:
            return 0
            
        if root in memory:
            return memory[root]
        
        op1 = root.data 
        
        if root.left != None:
            op1 += self.findMaxSum(root.left.left,memory)
            op1 += self.findMaxSum(root.left.right,memory)
        
        if root.right != None:
            op1 += self.findMaxSum(root.right.left,memory)
            op1 += self.findMaxSum(root.left.left,memory)
        
        
        op2 = self.findMaxSum(root.left,memory) + self.findMaxSum(root.right,memory)
        
        memory[root] = max(op1,op2)
        print(op1,op2)
        ans = max(op1,op2)
        # for key in memory:
            # print(key.data,"---->",memory[key])
        return ans
    
    
    def getMaxSum(self,root):
        
        memory = {}
        return self.findMaxSum(root,memory)
        