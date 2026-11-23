"""
SCS contains every character of both strings, but each shared character is written once instead of twice.
"""


class Solution:

    def minSuperSeq(self, s1, s2):

        memory = []
        for i in range(len(s1) + 1):
            currRow = []
            for j in range(len(s2) + 1):
                currRow.append(0)
            memory.append(currRow)

        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):

                if s1[i - 1] == s2[j - 1]:
                    memory[i][j] = 1 + memory[i - 1][j - 1]

                else:
                    memory[i][j] = max(memory[i - 1][j], memory[i][j - 1])

        i, j = len(s1), len(s2)
        scs = ""

        while i != 0 and j != 0:

            if s1[i - 1] == s2[j - 1]:
                scs += s1[i - 1]
                i -= 1
                j -= 1

            elif memory[i - 1][j] > memory[i][j - 1]:
                scs += s1[i - 1]
                i -= 1

            else:
                scs += s2[j - 1]
                j -= 1

        while i > 0:
            scs += s1[i - 1]
            i -= 1

        while j > 0:
            scs += s2[j - 1]
            j -= 1

        return scs[::-1]


s = Solution()
print(s.minSuperSeq(s1="geek", s2="eke"))