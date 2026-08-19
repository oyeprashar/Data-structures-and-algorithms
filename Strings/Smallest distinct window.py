"""
Input: str = "aabcbcdbca"
Output: 4
Explanation: Sub-String "dbca" has the smallest length that contains all the characters of str.
"""


class Solution:
    def findSubString(self, string):

        targetDict = {}

        for char in string:
            targetDict[char] = 1

        targetCount = len(targetDict)
        currCount = 0
        currDict = {}
        i = j = 0
        smallestStart = None
        smallestEnd = None

        while not(j >= len(string) and currCount < targetCount):

            # expand using j
            if currCount < targetCount:

                newChar = string[j]
                j += 1

                if newChar in currDict:
                    currDict[newChar] += 1
                else:
                    currDict[newChar] = 1

                if newChar in targetDict and currDict[newChar] == targetDict[newChar]:
                    currCount += 1

            else:

                if smallestStart is None or (j - i) < smallestEnd - smallestStart:
                    smallestStart = i
                    smallestEnd = j

                oldChar = string[i]
                i += 1

                currDict[oldChar] -= 1

                if oldChar in targetDict and currDict[oldChar] < targetDict[oldChar]:
                    currCount -= 1


        if smallestEnd is None:
            return ""

        return string[smallestStart : smallestEnd]


s = Solution()
print(s.findSubString("aabcbcdbca"))
