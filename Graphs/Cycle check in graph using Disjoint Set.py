class Graph:

    def __init__(self,numofVertices):
        self.numofVertices = numofVertices
        self.edgeList = []

    def addEdgePair(self,u,v):
        pair = (u,v)
        self.edgeList.append(pair)

    def find(self,i,parentList):
        if parentList[i] == -1:
            return i
        return self.find(parentList[i],parentList)

    def union(self,item1,item2,parentList):
        parentOfItem1 = self.find(item1,parentList)
        parentOfItem2 = self.find(item2,parentList)
        parentList[parentOfItem1] = parentOfItem2

    def cycleCheckDSU(self):
        parentList = [-1] *self.numofVertices
        for pair1 in self.edgeList:
            parent1 = self.find(pair1[0],parentList)
            parent2 = self.find(pair1[1],parentList)
            if parent1 != parent2:
                self.union(parent1,parent2,parentList)
            else:
                print("Same parents " + str(parent1) + " and " + str(parent2))
                return True

        return False
g = Graph(6)
g.addEdgePair(0,1)
g.addEdgePair(1,2)
g.addEdgePair(2,3)
g.addEdgePair(3,0)
print(g.edgeList)
g.cycleCheckDSU()