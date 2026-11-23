class Solution:

    def getLCSLen(self, s1, s2):

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
                    memory[i][j] = max(memory[i][j - 1], memory[i - 1][j])

        i, j = len(s1), len(s2)
        return memory[i][j]


    def minDeletions(self, s):
        return abs(len(s) - self.getLCSLen(s, s[::-1]))
