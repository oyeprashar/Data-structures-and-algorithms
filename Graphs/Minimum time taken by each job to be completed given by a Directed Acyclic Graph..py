"""
addEdge(1, 3);
addEdge(1, 4);
addEdge(1, 5);
addEdge(2, 3);
addEdge(2, 8);
addEdge(2, 9);
addEdge(3, 6);
addEdge(4, 6);
addEdge(4, 8);
addEdge(5, 8);
addEdge(6, 7);
addEdge(7, 8);
addEdge(8, 10);
"""
from collections import defaultdict

class Graph:
    
    def __init__(self,V):
        self.V = V
        self.vertList = defaultdict(list)
    
    def addEdge(self,u,v):
        self.vertList[u].append(v)

    
    def DFS_relax(self,currV,visited,value):

        visited.add(currV)
        currValue = value[currV]

        for nbr in self.vertList[currV]:

            if nbr not in visited:
                value[nbr] = max(value[nbr], currValue + 1)
                self.DFS_relax(nbr,visited,value)
            
    

    def ordering(self):

        value = [1] * (self.V+1)

        for currV in range(1,self.V+1):
            if value[currV] == 1:

                visited = set()
                self.DFS_relax(currV,visited,value)

        return value[1:]


        
        
g1 = Graph(10)

g1.addEdge(1, 3)
g1.addEdge(1, 4)
g1.addEdge(1, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 8)
g1.addEdge(2, 9)
g1.addEdge(3, 6)
g1.addEdge(4, 6)
g1.addEdge(4, 8)
g1.addEdge(5, 8)
g1.addEdge(6, 7)
g1.addEdge(7, 8)
g1.addEdge(8, 10)

# print(g1.vertList)
print(g1.ordering())