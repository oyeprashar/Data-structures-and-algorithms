#User function Template for python3

from collections import defaultdict

class Solution:
    
    def topologicalSort(self,currV,adj,visited,ordering):
        
        visited.add(currV)
        
        for nbr in adj[currV]:
            if nbr not in visited:
                self.topologicalSort(nbr,adj,visited,ordering)
            
        ordering.append(currV)
                
    def findOrder(self, dictionary, N, K):
        
        adj = defaultdict(list)
        
        for i in range(len(dictionary)-1):
            
            word1 = dictionary[i]
            word2 = dictionary[i+1]
            
            size = min(len(word1),len(word2))
            
            for j in range(size):
                
                if word1[j] != word2[j]:
                    adj[word1[j]].append(word2[j])
                    
                    break
      
        visited = set()
        ordering = []
        
        
        for x in range(K):
            char = chr(ord('a') + x)
            
            if char not in  visited:
                self.topologicalSort(char,adj,visited,ordering)
                
        
        return ordering[::-1]

