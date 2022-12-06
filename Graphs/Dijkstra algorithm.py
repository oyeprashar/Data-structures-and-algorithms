INT_MAX = 3**38

class Solution:
    
    def getMinV(self,dist,visited):
        
        minCost = 3**38
        minV = -1
        for i in range(len(dist)):
            if dist[i] < minCost and i not in visited:
                minCost = dist[i]
                minV = i
            
        return minV,minCost
        
    def dijkstra(self, V, adj, S):
        
        dist = [INT_MAX] * (V)
        visited = set()
        dist[S] = 0
        
        for _ in range(V):
            currV,currCost = self.getMinV(dist,visited)
            visited.add(currV)
            
            for nbr,edgeCost in adj[currV]:
                if dist[nbr] > currCost + edgeCost:
                    dist[nbr] = currCost + edgeCost
                
        return dist
            
            