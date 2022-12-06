class Solution:

    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        tDict = {}
        for char in t:
            if char not in tDict:
                tDict[char] = 1
            else:
                tDict[char] += 1

        reqCount = len(tDict)

        count = 0
        sDict = {}
        ans = [3 ** 38, ""]
        left = 0
        right = 0

        while True:

            if count < reqCount and right == len(s):
                break

            if count < reqCount:
                char = s[right]

                if char not in sDict:
                    sDict[char] = 1
                else:
                    sDict[char] += 1

                if char in t and sDict[char] == tDict[char]:
                    count += 1

                right += 1

            if count == reqCount:
                currStr = s[left:right]

                if len(currStr) < ans[0]:
                    ans[0] = len(currStr)
                    ans[1] = currStr

                char = s[left]

                sDict[char] -= 1

                if char in t and sDict[char] < tDict[char]:
                    count -= 1

                left += 1

        return ans[1]
