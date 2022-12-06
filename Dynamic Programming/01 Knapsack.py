class Solution:

    def knapSackHelper(self, W, wt, val, n, memory):

        if n == 0 or W == 0:
            return 0

        if wt[n - 1] > W:
            memory[W][n] = self.knapSackHelper(W, wt, val, n - 1, memory)
            return memory[W][n]

        if memory[W][n] != -1:
            return memory[W][n]

        memory[W][n] = max(val[n - 1] + self.knapSackHelper(W - wt[n - 1], wt, val, n - 1, memory),self.knapSackHelper(W, wt, val, n - 1, memory))
        return memory[W][n]

    def knapSack(self, W, wt, val, n):

        memory = []
        for x in range(W + 1):
            list1 = []
            for y in range(n + 1):
                list1.append(-1)
            memory.append(list1)

        return self.knapSackHelper(W, wt, val, n, memory)