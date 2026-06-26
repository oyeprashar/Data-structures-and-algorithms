"""
In this question we have to maximise the min valid distance
"""

class Solution:

    
    def isValid(self, minDistanceLimit, stalls, numOfCows):

        # since the array is sorted, placing the first cow on the zeroth index gives the largest room for 
        # other cowss
        lastCowPostion = 0
        placedCows = 1

        for i in range(1, len(stalls)):

            # place a cow if current min distance obeyed
            if stalls[i] - stalls[lastCowPostion] >= minDistanceLimit:
                placedCows += 1
                lastCowPostion = i

        return placedCows >= numOfCows


    def binarySearchOnAnswer(self, left, right, stalls, numOfCows, res):

        if left <= right:

            mid = (left + right) // 2

            # if the distance is valid, save it and maximise it
            if self.isValid(mid, stalls, numOfCows):
                res[0] = max(res[0], mid) # save the answer
                # move right to maximise this distance
                return self.binarySearchOnAnswer(mid + 1, right, stalls, numOfCows, res)

            else:
                return self.binarySearchOnAnswer(left, mid - 1, stalls, numOfCows, res)


    def placeCows(self, stalls, numOfCows):
        stalls.sort()
        res = [-3**38]
        maximumDist = stalls[-1] - stalls[0]
        self.binarySearchOnAnswer(0, maximumDist, stalls, numOfCows, res)
        return res[0]

test_cases = int(input())
s = Solution()
for _ in range(test_cases):
    n,numCows = map(int,input().split())
    stalls = []
    for i in range(n):
        x = int(input())
        stalls.append(x)
    print(s.placeCows(stalls, numCows))
