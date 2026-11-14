"""
Time complexity :
    Branching factor : k (we try all the colors)
    Number of times we do this : n (since we try for all the nodes)

    Work done at each call = O(k * n) <-- the two nested loops

    TC : O(k^n * k*n)
"""



class Solution:

    def isPossibleToColor(self, currV, nodesToColor, k, adj):

        if currV == len(adj):
            return True

        for color in range(k):

            isAvailable = True


            # check if there is a nbr using this color
            # if there is a nbr using this color, we break and go check other color
            for nbr in adj[currV]:

                if nodesToColor[nbr] == color:
                    isAvailable = False
                    break


            if isAvailable:

                # try the available color
                nodesToColor[currV] = color

                # can we successfully paint the entire graph ?
                if self.isPossibleToColor(currV + 1, nodesToColor, k, adj):
                    return True

                # remove the color since we were not able to color the entire graph
                nodesToColor[currV] = -1


        return False

    def graphColoring(self,adj, m):

        nodesToColor = [-1] * len(adj)
        return self.isPossibleToColor(0, nodesToColor, m, adj)

s = Solution()
print(s.graphColoring(adj = [[1, 3, 2], [0, 3], [3, 0], [1, 2, 0]], m = 3))
