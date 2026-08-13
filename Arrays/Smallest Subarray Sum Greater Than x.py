class Solution:
    def smallestSubWithSum(self, target, arr):

        i = 0  # <--- used for skrinking
        j = 0  # <--- used for expanding
        currSum = 0
        currSize = 0
        minSize = 3 ** 38

        while not (currSum <= target and j >= len(arr)): # if this condition occurs, we cannot explore more!
            # so this while condition allows us to explore all the possible cases!

            if currSum <= target:
                # expand
                currSum += arr[j]
                j += 1
                currSize += 1
            else:
                # save and skrink
                minSize = min(minSize, currSize)
                currSum -= arr[i]
                i += 1
                currSize -= 1

        if minSize >= 3 ** 38:
            return 0

        return minSize



