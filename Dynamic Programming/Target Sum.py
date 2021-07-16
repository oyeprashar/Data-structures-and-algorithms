class Solution:

    def isPossible(self, i, t, currSetSum, nums, memory):

        if i == len(nums) and currSetSum == t:
            return 1

        if i == len(nums) and currSetSum != t:
            return 0

        if memory[i][currSetSum] != -1:
            return memory[i][currSetSum]

        memory[i][currSetSum] = self.isPossible(i + 1, t, currSetSum + nums[i], nums, memory) + self.isPossible(i + 1,
                                                                                                                t,
                                                                                                                currSetSum,
                                                                                                                nums,
                                                                                                                memory)

        return memory[i][currSetSum]

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        i = 0
        totalSum = sum(nums)
        currSetSum = 0
        t = (totalSum - target) / 2

        memory = []
        for x in range(len(nums) + 1):
            list1 = []
            for y in range(totalSum + 1):
                list1.append(-1)
            memory.append(list1)

        return self.isPossible(i, t, currSetSum, nums, memory)