class Solution:
    
    def DFS(self,currV,visited2,revAdj):
        
        visited2.add(currV)
        
        for nbr in revAdj[currV]:
            if nbr not in visited2:
                self.DFS(nbr,visited2,revAdj)
            
    def finDFS(self,currV,visited,list1,adj):
        
        visited.add(currV)
        
        for nbr in adj[currV]:
            if nbr not in visited:
                self.finDFS(nbr,visited,list1,adj)
            
        list1.append(currV)
        
    def kosaraju(self, V, adj):
        
        list1 = []
        visited = set()
        for currV in range(V):
            if currV not in visited:
                self.finDFS(currV,visited,list1,adj)
                
        revAdj = []
        for _ in range(len(adj)):
            row = []
            revAdj.append(row)
        
        for i in range(len(adj)):
            for item in adj[i]:
                revAdj[item].append(i)
                

        visited2 = set()
        count = 0
        while len(list1) > 0:
            currV = list1.pop()
            if currV not in visited2:
                count += 1
                self.DFS(currV,visited2,revAdj)
            

        return count