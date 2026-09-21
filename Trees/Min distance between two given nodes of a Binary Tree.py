
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def build_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

class Solution:

    # this returns back the number of nodes but we want the number of edges and hence we subtract 1
    def computeDistance(self, root, target):

        if root is None:
            return -3**38

        if root.data == target:
            return 1

        return 1 + max(self.computeDistance(root.left, target), self.computeDistance(root.right, target))


    def getLCA(self, root, node1, node2):

        if root is None:
            return None

        if root.data == node1 or root.data == node2:
            return root

        leftRes = self.getLCA(root.left, node1, node2)
        rightRes = self.getLCA(root.right, node1, node2)

        if leftRes is not None and rightRes is not None:
            return root

        if leftRes is not None:
            return leftRes

        if rightRes is not None:
            return rightRes

        return None


    def findDist(self, root, node1, node2):

        lcaNode = self.getLCA(root, node1, node2)

        dist1 = self.computeDistance(lcaNode, node1)
        dist2 = self.computeDistance(lcaNode, node2)

        return dist1 + dist2 - 2



testRoot =  build_tree()

s = Solution()
print(s.findDist(testRoot, 4, 7))
