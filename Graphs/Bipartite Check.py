class Solution:
    
    def isPossible(self,src,colored,adj):

        queue = [src]

        while len(queue) > 0:

            currV = queue.pop(0)

            availableCOlor = [True,True]

            for nbr in adj[currV]:

                if colored[nbr] == -1:
                    queue.append(nbr)

                else:
                    if colored[nbr] == 0:
                        availableCOlor[0] = False

                    elif colored[nbr] == 1:
                        availableCOlor[1] = False

            selectedColor = None
            for i in range(len(availableCOlor)):
                if availableCOlor[i] == True:
                    selectedColor = i
                    break 

            if selectedColor == None:
                return False

            colored[currV] = selectedColor 

        return True 
        
    def isBipartite(self, V, adj):
        
        n = len(adj)
        colored = [-1] * n 

        for currV in range(n):
            if colored[currV] == -1:
                if self.isPossible(currV,colored,adj) == False:
                    return False 

        return True 