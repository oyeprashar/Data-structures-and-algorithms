"""
    src -> layover -> dst
    k means the number of stops between src and dst, and the edges needed to process it is k + 1


    Approach :

        1. We need to make sure that the weights are not propagated across the nodes, and we need to control this
           layer by layer. <--- To ensure the k stops constraint
        2. To make sure that the new weights are not affecting other weights, we do not write directly to min dist.
        3. We read from minDist and write to temp.
        4. After a layer is processed, we update the value in minDist.
        5. This makes sure that the last layer weights affect the current computation and weights from current
           computation is not affecting distances.
"""

INT_MAX = 3 ** 38


class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):

        minDist = [INT_MAX] * n
        temp = [INT_MAX] * n
        minDist[src] = 0
        temp[src] = 0

        for _ in range(k + 1):

            for flight in flights:

                u = flight[0]
                v = flight[1]
                edgeCost = flight[2]

                if minDist[u] != INT_MAX:
                    temp[v] = min(temp[v], minDist[u] + edgeCost)

            for i in range(len(minDist)):
                minDist[i] = temp[i]

        if minDist[dst] == INT_MAX:
            return -1

        return minDist[dst]


