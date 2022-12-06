# TIME COMPLEXITY : O(N^2) | SPACE COMPLEXITY : O(N^2)

class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):

        memory = []
        for x in range(len(S1) + 1):
            list1 = []
            for y in range(len(S2) + 1):
                list1.append(-1)
            memory.append(list1)

        ans = 0

        for i in range(len(S1) + 1):
            for j in range(len(S2) + 1):

                if i == 0 or j == 0:
                    memory[i][j] = 0

                elif S1[i - 1] == S2[j - 1]:
                    memory[i][j] = memory[i - 1][j - 1] + 1
                    ans = max(ans, memory[i][j])

                else:
                    memory[i][j] = 0
        return ans