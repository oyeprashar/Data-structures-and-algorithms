"""
Finding the LCA in n-array
"""

from collections import defaultdict

class Tree:

    def __init__(self,size):
        self.size = size 
        self.adj = defaultdict(list)

    def addNode(self,parent,child):
        self.adj[parent].append(child)

# TC: O(N) SC: O(H)
def findPath(root,target,currPath,ansPath,adj):

    if root == target:
        ansPath.extend(currPath.copy())
        ansPath.append(target)
        return

    currPath.append(root)
    for child in adj[root]:
        findPath(child,target,currPath,ansPath,adj)
    currPath.pop()


# TC: O(H)
def findLCA(root,data1,data2,adj):

    path1 = []
    path2 = []
    findPath(root,data1,[],path1,adj)
    findPath(root,data2,[],path2,adj)

    if len(path1) == 0 or len(path2) == 0:
        return '-1' 

    i = len(path1) - 1
    j = len(path2) - 1 

    while i >= 0 and j >= 0:
        if path1[i] == path2[j]:
            return path1[i]

        i -= 1 
        j -= 1 

    return '-1'

currTree = Tree(10)
currTree.addNode(1,2)
currTree.addNode(1,3)
currTree.addNode(1,4)
currTree.addNode(3,5)
currTree.addNode(3,6)
currTree.addNode(3,7)
currTree.addNode(3,8)
currTree.addNode(4,9)
currTree.addNode(4,10)


print(findLCA(1,5,9,currTree.adj))
print(findLCA(1,5,8,currTree.adj))
print(findLCA(1,9,10,currTree.adj))
