# User function Template for python3
class Solution:

    def coutSubsetWithTargetSum(self, currIndex, arr, targetSum, memory):

        # This handles the case where the input targetSum was itself == 0 
        # This allows the code to explore paths and not return 1 just because the input was zero!
        if currIndex == len(arr):
            if targetSum == 0:
                return 1
            return 0

        if currIndex > len(arr):
            return 0

        if targetSum - arr[currIndex] < 0:
            return self.coutSubsetWithTargetSum(currIndex + 1, arr, targetSum, memory)

        if memory[currIndex][targetSum] != -1:
            return memory[currIndex][targetSum]

        op1 = self.coutSubsetWithTargetSum(currIndex + 1, arr, targetSum - arr[currIndex], memory)
        op2 = self.coutSubsetWithTargetSum(currIndex + 1, arr, targetSum, memory)

        memory[currIndex][targetSum] =  op1 + op2
        return memory[currIndex][targetSum]

    def perfectSum(self, arr, target):

        memory = []
        for i in range(len(arr)):
            currRow = []
            for j in range(target + 1):
                currRow.append(-1)
            memory.append(currRow)


        return self.coutSubsetWithTargetSum(0, arr, target, memory)
