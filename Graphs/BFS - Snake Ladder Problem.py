from collections import defaultdict

class Solution:
    def minThrow(self, N, arr):
        
        specialThrows = {}
        i = 0
        
        while i < len(arr):
            specialThrows[arr[i]] = arr[i+1]
            i += 2

        adj = defaultdict(list)

        for cell in range(1,31):
            for diceNumber in range(1,7):
                
                canReach = cell + diceNumber
                
                if canReach <= 30:
                    
                    if canReach in specialThrows:
                        adj[cell].append(specialThrows[canReach])
                    else:
                        adj[cell].append(canReach)
        
        count = 0
        
        queue = [1]
        
        while len(queue) > 0:
            
            size = len(queue)
            count += 1
            
            for _ in range(size):
                
                curr = queue.pop(0)
                
                for nbr in adj[curr]:
                    
                    if nbr >= 30:
                        return count 
                    queue.append(nbr) 
        
        return -1 
    
                