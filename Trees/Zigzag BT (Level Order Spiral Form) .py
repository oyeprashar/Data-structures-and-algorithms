class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self,root):
        
        if root == None:
            return []
            
        ans = []
        queue = [root]
        currLevel = [root.data]
        flag = False
        
        while len(queue) != 0:
            
            if flag == True:
                ans.extend(currLevel[::-1])
                flag = False
            else:
                ans.extend(currLevel)
                flag = True
            
            currLevel = []
            
            size = len(queue)
            
            for _ in range(size):
                
                curr = queue.pop(0)
                
                if curr.left != None:
                    queue.append(curr.left)
                    currLevel.append(curr.left.data)
                if curr.right != None:
                    queue.append(curr.right)
                    currLevel.append(curr.right.data)
                    
            
        return ans