class Solution:

    def isPalindrome(self, i, j, str1):
        checkStr = str1[i:j + 1]
        return checkStr == checkStr[::-1]

    def helper(self, i, j, str1, memory):

        if i >= j or self.isPalindrome(i, j, str1) is True:
            return 0

        if memory[i][j] != -1:
            return memory[i][j]

        ans = 3 ** 38
        for K in range(i, j):
            op1 = self.helper(i, K, str1, memory)
            op2 = self.helper(K + 1, j, str1, memory)

            res = op1 + 1 + op2
            ans = min(res, ans)

        memory[i][j] = ans
        return ans

    def palindromicPartition(self, str1):
        memory = []
        for x in range(len(str1) + 1):
            list1 = []
            for y in range(len(str1) + 1):
                list1.append(-1)
            memory.append(list1)

        i = 0
        j = len(str1) - 1
        return self.helper(i, j, str1, memory)


s = Solution()
print(s.palindromicPartition("geeek"))