"""
When you cut the board vertically, the cut runs through all the horizontal pieces and we increase the number of vertical pieces

Greedy Approach :
    - We want to use the costlier cuts when the number pieces are less!
    - This way the total cost is minimised

"""

class Solution:
    def minCost(self, n, m, costVertical, costHorizontal):

        costVertical.sort(reverse = True)
        costHorizontal.sort(reverse = True)
        verticalPieces = 1
        horizontalPieces = 1

        i = 0
        j = 0
        totalCost = 0

        while i < len(costVertical) and j < len(costHorizontal):

            if costVertical[i] > costHorizontal[j]:
                totalCost += (costVertical[i] * horizontalPieces)
                verticalPieces += 1
                i += 1

            else:
                totalCost += (costHorizontal[j] * verticalPieces)
                horizontalPieces += 1
                j += 1


        while i < len(costVertical):
            totalCost += (costVertical[i] * horizontalPieces)
            verticalPieces += 1
            i += 1

        while j < len(costHorizontal):
            totalCost += (costHorizontal[j] * verticalPieces)
            horizontalPieces += 1
            j += 1

        return totalCost
        
