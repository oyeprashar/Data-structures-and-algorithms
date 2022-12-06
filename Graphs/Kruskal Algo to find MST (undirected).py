"""
Kruskal MST
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
"""

from ast import parse


def find(num, parentList):
    if parentList[num] == -1:
        return num 
    
    parentList[num] = find(parentList[num],parentList)

    return parentList[num]

def union(num1, num2, rankList, parentList):

    parent1 = find(num1, parentList)
    parent2 = find(num2, parentList)

    if parent1 != parent2:
        # smaller rank ka parent is element with bigger rank
        if rankList[parent2] < rankList[parent1]:
            parentList[parent2] = parent1
            rankList[parent1] += rankList[parent2]
        
        else:
            parentList[parent1] = parent2
            rankList[parent2] += rankList[parent1]

class Graph:
    def __init__(self,V):
        self.V = V
        self.vertList = []
    
    def addEdge(self,u,v,cost):
        self.vertList.append((u,v,cost))
    
    def kruskal(self):

        print(self.vertList)

        parentList = [-1] * self.V
        rankList = [1] * self.V
        count = 0 
        index = 0 
        cost = 0
        self.vertList.sort(key = lambda list1 : list1[2])

        while count != self.V - 1 and index < len(self.vertList):
            
            list1 = self.vertList[index]
            u = list1[0]
            v = list1[1]
            currCost = list1[2]

            parent1 = find(u,parentList)
            parent2 = find(v,parentList)
        
            if parent1 != parent2:
                print("picking up edge between",u,v,"with cost =",currCost)
                count += 1 
                union(parent1,parent2,rankList,parentList)
                cost += currCost

            index += 1

        return cost
        

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)


print(g.kruskal())
