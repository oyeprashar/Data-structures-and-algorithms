
class Solution:

    def minWindow(self, string1, targetString):

        targetDict = {}
        for char in targetString:
            if char not in targetDict:
                targetDict[char] = 1
            else:
                targetDict[char] += 1

        # this is not what it looks like ;)
        targetCount = len(targetDict)
        currCount = 0
        currDict = {}
        i = j = 0

        smallestStart = None
        smallestEnd = None

        # We will add a condition here
        while not(j == len(string1) and currCount < targetCount):


            # expand using j
            if currCount < targetCount:
                newChar = string1[j]
                j += 1

                if newChar in currDict:
                    currDict[newChar] += 1
                else:
                    currDict[newChar] = 1

                if newChar in targetDict and currDict[newChar] == targetDict[newChar]:
                    currCount += 1

            else:
                if smallestStart is None or (j - i) < (smallestEnd - smallestStart):
                    smallestStart = i
                    smallestEnd = j


                # we skrink using ith pointer
                char = string1[i]
                i += 1

                currDict[char] -= 1

                # it is okay to have more frequency in the currDict but not less!
                if char in targetDict and currDict[char] < targetDict[char]:
                    currCount -= 1


        if smallestStart is None or smallestEnd is None:
            return ""

        return string1[smallestStart:smallestEnd]
