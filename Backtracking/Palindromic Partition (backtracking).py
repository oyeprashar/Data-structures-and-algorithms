"""
NOTE : There is a DP solution to this! This is naive backtracking

Time Complexity :
    - We have 2 options at each index, either break from here or dont == O(2^n)
    - We start a loop at each index and then from the word and check if its palindromic == O(n * (n + n)) == O(n^2)
    - Total time complexity = O(2^n * n^2)
"""



class Solution:

    def isPalindrome(self, string):

        i = 0
        j = len(string) - 1

        while i < j:
            if string[i] != string[j]:
                return False

            i += 1
            j -= 1

        return True


    def palindromicPartioning(self, currIndex, string, currSplit, res):

        # We were able to process the whole string
        if currIndex == len(string):
            res.append(currSplit.copy())
            return True

        # O(n^2)
        for i in range(currIndex, len(string)):
            currWord = string[currIndex : i + 1]
            if self.isPalindrome(currWord):
                currSplit.append(currWord)
                self.palindromicPartioning(i + 1, string, currSplit, res)
                currSplit.pop()


    def palinParts (self, s):
        res = []
        self.palindromicPartioning(0, s, [], res)
        return res


s = Solution()
print(s.palinParts("geeks"))
