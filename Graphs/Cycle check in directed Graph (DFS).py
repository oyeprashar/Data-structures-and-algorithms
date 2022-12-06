class Solution:

    def cycleDetectionDirectedDFS(self,currV,adj,visited,currPath):
        
        visited.add(currV)
        currPath[currV] = True
        
        for nbr in adj[currV]:
            
            if nbr not in visited:
                check = self.cycleDetectionDirectedDFS(nbr,adj,visited,currPath)
                if check == True:
                    return True
                
            else:
                if currPath[nbr] == True:
                    return True
            
        currPath[currV] = False
        return False

        
    def isCyclic(self, V, adj):
        visited = set()
        currPath = [False] * (V+1)
        
        for currV in range(V):
            if currV not in visited:
                ans = self.cycleDetectionDirectedDFS(currV,adj,visited,currPath)
                if ans == True:
                    return True

        return False

