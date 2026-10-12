class Solution:

    def isPossible(self, currIndex, arr, currSum, visited, k, target):

        # since sum(arr) % k == 0, now we can say the remaining elements can sum up to the target
        if k == 1: # even k == 0 would work just fine
            return True

        if currSum == target:
            return self.isPossible(0, arr, 0, visited, k - 1, target)

        if currIndex == len(arr):
            return False

        # if element is part of some other we skip it
        if visited[currIndex]:
            return self.isPossible(currIndex + 1, arr, currSum, visited, k, target)

        visited[currIndex] = True
        currSum += arr[currIndex]
        op1 = self.isPossible(currIndex + 1, arr, currSum, visited, k, target)

        # why waste time exploring op2
        if op1 is True:
            return True

        currSum -= arr[currIndex]
        visited[currIndex] = False

        op2 = self.isPossible(currIndex + 1, arr, currSum, visited, k, target)

        return op1 or op2

    def isPartK(self, arr, k):

        # if we cannot make divide the sum into k subsets, lets do early return
        if sum(arr) % k != 0 or len(arr) == 0:
            return False

        visited = [False] * len(arr)
        return self.isPossible(0, arr, 0, visited, k, sum(arr) // k)