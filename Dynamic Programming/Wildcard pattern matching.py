class Solution:
    def wildCard(self, str1, str2):
        text = str1
        pattern = str2

        memory = []
        for x in range(len(pattern) + 1):
            list1 = []
            for y in range(len(text) + 1):
                list1.append(False)
            memory.append(list1)

        memory[0][0] = True

        for p in range(1, len(pattern) + 1):
            if pattern[p - 1] == "*":
                memory[p][0] = memory[p - 1][0]

        for i in range(1, len(pattern) + 1):
            for j in range(1, len(text) + 1):

                if pattern[i - 1] == "?" or pattern[i - 1] == text[j - 1]:
                    memory[i][j] = memory[i - 1][j - 1]

                elif pattern[i - 1] == "*":
                    memory[i][j] = memory[i - 1][j] | memory[i][j - 1]

                elif pattern[i - 1] != text[j - 1]:
                    memory[i][j] = False

        return memory[i][j]