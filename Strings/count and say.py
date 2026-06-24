"""
Input: n = 4

Output: "1211"

Explanation:

countAndSay(1) = "1"
countAndSay(2) = RLE of "1" = "11"
countAndSay(3) = RLE of "11" = "21"
countAndSay(4) = RLE of "21" = "1211"
"""
    
class Solution:

    # Apply the rules to a single string
    # frequency + char
    def RLE(self, string):

        # lets say the number is 21
        prev = string[0]
        count = 1
        res = ""
        currIndex = 1

        while currIndex <= len(string):

            if currIndex == len(string):
                res += str(count)
                res += prev
                return res

            if string[currIndex] == prev:
                count += 1

            elif string[currIndex] != prev:
                res += str(count)
                res += prev
                count = 1
                prev = string[currIndex]

            currIndex += 1

        return res

    def countAndSay(self, n):

        if n == "1":
            return 1

        string = "1"
        for _ in range(n - 1):
            string = self.RLE(string)

        return string


s = Solution()
print(s.countAndSay(4)) # 1211
