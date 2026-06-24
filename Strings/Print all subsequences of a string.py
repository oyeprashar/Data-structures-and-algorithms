class Solution:

    def generate_subsets(self, currIndex, currArr, stringArr, res):
        
        # exhaust the possibilities for subset
        if currIndex == len(stringArr):
            res.append("".join(currArr))
            return

        # op1 : choose
        currArr.append(stringArr[currIndex])
        self.generate_subsets(currIndex + 1, currArr, stringArr, res)
        currArr.pop()

        # op2 : Skip
        self.generate_subsets(currIndex + 1, currArr, stringArr, res)


    def powerSet(self, s):
        res = []
        self.generate_subsets(0, [], list(s), res)
        return sorted(res)

s = Solution()
# Correct O/P : ["","a", "ab", "abc", "ac", "b", "bc", "c"]
print(s.powerSet("abc"))
