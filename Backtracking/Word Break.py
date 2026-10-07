"""
    Input: s = "leetcode", wordDict = ["leet","code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

The time complexity is O(n^2 * n)
"""


class Solution:

    def isPossibleToBreak(self, currIndex, string, dict, cache):

        if currIndex == len(string):
            return True

        if currIndex in cache:
            return cache[currIndex]

        for i in range(currIndex, len(string)):

            currWord = string[currIndex: i + 1]

            if currWord in dict:
                if self.isPossibleToBreak(i + 1, string, dict, cache):
                    cache[currIndex] = True
                    return cache[currIndex]

        cache[currIndex] = False
        return cache[currIndex]

    def wordBreak(self, s, wordDict):
        return self.isPossibleToBreak(0, s, set(wordDict), {})
