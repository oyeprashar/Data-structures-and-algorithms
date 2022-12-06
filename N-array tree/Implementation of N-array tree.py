from collections import defaultdict 

class NarrayTree:

    def __init__(self,size):
        self.size = size
        self.adj = defaultdict(list)

    def addNode(self,u,v):
        self.adj[u].append(v)


def DFS(currNode,visited,adj):

    print(currNode,end=" ")
    visited.add(currTree)

    for nbr in adj[currNode]:
        DFS(nbr,visited,adj)

currTree = NarrayTree(7)
currTree.addNode(1,2)
currTree.addNode(1,3)
currTree.addNode(2,4)
currTree.addNode(2,5)
currTree.addNode(2,6)
currTree.addNode(3,7)

visited = set()
DFS(1,visited,currTree.adj)