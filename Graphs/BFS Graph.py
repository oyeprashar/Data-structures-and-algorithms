class Solution:
    
    def bfsOfGraph(self, V, adj):
        
        visited = set()
        ans = []
        visited.add(0)
        queue = [0]
        
        
        while len(queue) > 0:
            
            curr = queue.pop(0)
            
            for nbr in adj[curr]:
                
                if nbr not in visited:
                    # as soon as a child is discovered, we add it to the visited to 
                    # avoid printing it again and again from other paths
                    visited.add(nbr)
                    ans.append(nbr)
                    queue.append(nbr)
    
        return ans