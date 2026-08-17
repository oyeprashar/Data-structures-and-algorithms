"""
The time complexity is O(n!)

    - Because even if we naively think mathematically, that's how permutations are genrated
    - We make n calls at n indices but that keep on decreasing at each level

        index 0 → n choices
        index 1 → n-1 choices
        index 2 → n-2 choices
        ...
        index n-1 → 1 choice

        That's total of n! choices

"""

class Solution:

    def generatePermutations(self, currIndex, stringList, res):

        if currIndex == len(stringList):
            res.append("".join(stringList))
            return

        for i in range(currIndex, len(stringList)):
            stringList[currIndex], stringList[i] = stringList[i], stringList[currIndex]
            self.generatePermutations(currIndex + 1, stringList, res)
            stringList[currIndex], stringList[i] = stringList[i], stringList[currIndex]

    def findPermutation(self, string):

        res = []
        self.generatePermutations(0, list(string), res)
        return list(set(res))