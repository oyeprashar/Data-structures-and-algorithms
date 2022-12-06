INT_MAX = 3**38
class Solution:
    
    def findCheapestPrice(self, n, flights, src, dst, k):
        
        cost = [INT_MAX] * n 
        temp = [INT_MAX] * n
        cost[src] = 0
        temp[src] = 0
        
        for _ in range(k+1):
            
            for flight in flights:
                u = flight[0]
                v = flight[1]
                edgeCost = flight[2]
                
                if cost[u]+edgeCost < temp[v]:
                    temp[v] = cost[u]+edgeCost
                                                
            for i in range(len(temp)):
                cost[i] = temp[i]
         
        if cost[dst] == INT_MAX:
            return -1

        return cost[dst]