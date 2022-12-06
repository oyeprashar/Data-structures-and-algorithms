from collections import defaultdict

class Solution:
    
    def verticalOrder(self, root): 
        
        if root == None:
            return []
        
        queue = [root]
        HD = {}
        HD[root] = 0
        
        levels = defaultdict(list)
        levels[0].append(root.data)
        
        while len(queue) != 0:
            
            curr = queue.pop(0)
            
            if curr.left != None:
                queue.append(curr.left)
                parentHD = HD[curr]
                HD[curr.left] = parentHD - 1
                levels[HD[curr.left]].append(curr.left.data)
            
            if curr.right != None:
                queue.append(curr.right)
                parentHD = HD[curr]
                HD[curr.right] = parentHD + 1
                levels[HD[curr.right]].append(curr.right.data)
            
        
        ans = []
        
        for key in sorted(levels):
            currList = levels[key]
            
            for item in currList:
                ans.append(item)
        
        return ans
                