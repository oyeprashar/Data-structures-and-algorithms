"""
Clone graph
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


#### TODO : Most important part is the graph is connected!

class Solution:

    def cloneGraphDFS(self, currNode, visited, clonedNodesDict):

        if currNode is None:
            return None

        visited.add(currNode)

        if currNode.val not in clonedNodesDict:
            clonedNodesDict[currNode.val] = Node(currNode.val)

        parentCloneNode = clonedNodesDict[currNode.val]
        clonedNeighbors = []

        for nbr in currNode.neighbors:

            if nbr.val not in clonedNodesDict:
                clonedNodesDict[nbr.val] = Node(nbr.val)

            clonedNeighbors.append(clonedNodesDict[nbr.val])

            if nbr not in visited:
                self.cloneGraphDFS(nbr, visited, clonedNodesDict)

        parentCloneNode.neighbors = clonedNeighbors

        return parentCloneNode

    def cloneGraph(self, node):
        return self.cloneGraphDFS(node, set(), {})
