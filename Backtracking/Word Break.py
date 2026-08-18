"""
    Input: s = "ilike", dictionary[] = ["i", "like", "gfg"]
    Output: true
    Explanation: s can be breakdown as "i like".

    Naive TC : O(2^n) because a | b | c | d <----- we are asking at each index if we want to make a cut or not
    Optimised TC :  cached/dp solution work in O(n^2) <--- to fill each cache index (linear size n) we run a linear loop
"""


class Solution:


    def wordBreakHelper(self, currIndex, string, wordSet, cache):

        if currIndex == len(string):
            return True

        if cache[currIndex] != -1:
            return cache[currIndex]


        """
        The loop runs till len(string) + 1 -> meaning len(string) because when we sice [x:y] then y is not included
        and the base case is when currIndex == len(string)
        """
        for i in range(currIndex + 1, len(string) + 1):

            currWord = string[currIndex:  i]

            if currWord in wordSet:

                # since the index i was not included the currWord, we make the next call using it
                if self.wordBreakHelper(i, string, wordSet, cache):
                    cache[currIndex] =  True
                    return cache[currIndex]

        cache[currIndex] = False
        return cache[currIndex]

    def wordBreak(self, s, dictionary):
        wordSet = set(dictionary)

        cache = [-1] * (len(s) + 1)

        return self.wordBreakHelper(0, s, wordSet, cache)

s = Solution()
print(s.wordBreak(s = "ilike",dictionary= ["i", "like", "gfg"]))