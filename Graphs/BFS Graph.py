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

                    # we want to ensure that nodes is enqueue once. Because lets say two nodes were connected to a node 3
                    # then node 3 will be added to the queue twice if we pop and mark visited. To avoid it and to ensure
                    # we only add a node to the queue once, we mark a node visited as soon as it is enqueued to the queue
                    visited.add(nbr)
                    ans.append(nbr)
                    queue.append(nbr)
    
        return ans