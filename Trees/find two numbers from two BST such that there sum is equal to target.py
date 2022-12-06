class Solution:
    def generateDict(self,root1,tree1Dict):
        
        if root1 != None:
            
            self.generateDict(root1.left,tree1Dict)
            
            if root1.data in tree1Dict:
                tree1Dict[root1.data] += 1
            else:
                tree1Dict[root1.data] = 1
            
            self.generateDict(root1.right,tree1Dict)
            
    def countingPairs(self,root2,count,x,tree1Dict):
        
        if root2 != None:
            
            self.countingPairs(root2.left,count,x,tree1Dict)
            
            target = x - root2.data
            if target in tree1Dict:
                count[0] += 1
            
            self.countingPairs(root2.right,count,x,tree1Dict)
            
        
    def countPairs(self, root1, root2, x): 
        
        tree1Dict = {}
        self.generateDict(root1,tree1Dict)

        count = [0]
        
        self.countingPairs(root2,count,x,tree1Dict)
        
        return count[0]