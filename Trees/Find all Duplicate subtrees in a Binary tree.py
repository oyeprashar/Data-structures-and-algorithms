"""
In this problem, even a single node is considered as a subtree! So base case includes just the null nodes because
we want to want to write just the null nodes in the freq dict and call them duplicates!
"""

''' Structure of a Tree Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''


class Solution:

    def printAllDupsHelper(self, root, freq, ans):

        # Single null nodes are not written in the freq dict because of this return
        # but leaf nodes will be written in dict since no return
        if root is None:
            return "X"

        leftRes = self.printAllDupsHelper(root.left, freq, ans)
        rightRes = self.printAllDupsHelper(root.right, freq, ans)
        currSubTree = "(" + leftRes + ")" + str(root.data) + "(" + rightRes + ")"

        if currSubTree in freq:
            freq[currSubTree] += 1
        else:
            freq[currSubTree] = 1


        """
        Why == 2?
          Because if we say `freq[currSubTree] > 1` then everytime a subtree repeats (after freq 2) we will add it to ans
          and that will be wrong. We want to add the root to the ans once if it is duplicate
        """
        if freq[currSubTree] == 2:
            ans.append(root.data)

        return currSubTree

    def printAllDups(self, root):
        freq = {}
        ans = []
        self.printAllDupsHelper(root, freq, ans)
        return ans


