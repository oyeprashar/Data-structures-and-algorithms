from collections import defaultdict

class Solution:
    def DFS(self,currV,visited,lastVisited,minEdge,adj):
        
        visited.add(currV)
        lastVisited[0] = currV
        
        for list1 in adj[currV]:
            
            nbr = list1[0]
            
            if nbr not in visited:
                cost = list1[1]
                minEdge[0] = min(minEdge[0],cost)
                
                self.DFS(nbr,visited,lastVisited,minEdge,adj)


    def solve(self, n, p ,a, b, d): 
        
        adj = defaultdict(list)
        
        for i in range(len(a)):
            adj[a[i]].append((b[i],d[i]))
        
        visited = set()
        
        startSet = set(a)
        endSet = set(b)
        
        startingPoint = []
        
        # the nodes which are in the start list and not in the end list tells us that these
        # are the start of some connected component
        for item in startSet:
            if item not in endSet:
                startingPoint.append(item)
        
        ans = []
      
        
        for currV in startingPoint:
            if currV not in visited:
                minEdge = [3**38]
                lastVisited = [None]
                
                self.DFS(currV,visited,lastVisited,minEdge,adj)
                ans.append([currV,lastVisited[0],minEdge[0]])
        

        
        return ans
        