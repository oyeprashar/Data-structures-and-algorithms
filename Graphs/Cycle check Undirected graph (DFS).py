class Solution:
    
    def detectCycleDFS(self,currV,adj,visited,parentList):
        
        visited.add(currV)
        nbrList = adj[currV]
        
        for nbr in nbrList:
            
            if nbr not in visited:
                #  update parent and call recursively
                parentList[nbr] = currV
                check = self.detectCycleDFS(nbr,adj,visited,parentList)
                if check == True:
                    return True
                
            else:
                # check is visited node curr ka parent to nhi
                if parentList[currV] != nbr:
                    return True
                
        return False
        
        
    def isCycle(self, V, adj):
        visited = set()
        parentList = [-1] * (V+1)
        
        for currV in range(V):
            if currV not in visited:
                ans = self.detectCycleDFS(currV,adj,visited,parentList)
                if ans == True:
                    return True
                   
        return False