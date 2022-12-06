from collections import defaultdict

class Solution:

    def find(self,num, parentList):

        if parentList[num] == -1:
            return num  

        parentList[num] = self.find(parentList[num], parentList)

        return parentList[num]

    def union(self,num1, num2, rankList, parentList):

        parent1 = self.find(num1, parentList)
        parent2 = self.find(num2, parentList)

        if parent1 != parent2:

            if rankList[parent1] > rankList[parent2]:
                parentList[parent2] = parent1 
                rankList[parent1] += rankList[parent2]

            else:
                parentList[parent1] = parent2
                rankList[parent2] += rankList[parent1]

    def DFS(self,currV,adj,visited):

        visited.add(currV)

        for nbr in adj[currV]:
            if nbr not in visited:
                self.DFS(nbr,adj,visited)


    def neededConnections(self,arr,n):
        count = 0
        rankList = [1] * n
        parentList = [-1] * n

        for edge in arr:
            u = edge[0]
            v = edge[1]

            if self.find(u,parentList) != self.find(v,parentList):
                self.union(u,v,rankList,parentList)
                count += 1 

        return count 


    def disconnectedComputers(self,arr,n):

        adj = defaultdict(list)	

        for edge in arr:
            u = edge[0]
            v = edge[1]

            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        disconnected = 0


        for currV in range(n):

            if currV not in visited:
                disconnected += 1 
                self.DFS(currV,adj,visited) 

        return disconnected - 1
    
    def makeConnected(self, n, connections):
        
        totalConnection = len(connections)
        needed = self.neededConnections(connections,n)
        disconnectedCount = self. disconnectedComputers(connections,n)
        
        available = totalConnection - needed 
        
        if disconnectedCount > available:
            return -1 
        
        else:
            return disconnectedCount
        