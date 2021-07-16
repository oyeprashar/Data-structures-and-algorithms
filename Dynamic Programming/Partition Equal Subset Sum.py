class Solution:

    def isPossible(self, i, target, arr, memory):

        if target == 0:
            return True

        elif i == len(arr) and target != 0:
            return False

        if memory[i][target] != -1:
            return memory[i][target]

        else:

            memory[i][target] = self.isPossible(i + 1, target - arr[i], arr, memory) | self.isPossible(i + 1, target,
                                                                                                       arr, memory)
            return memory[i][target]

    def canPartition(self, nums: List[int]) -> bool:
        sum1 = sum(nums)
        if sum1 % 2 != 0:
            return 0

        target = sum1 // 2

        memory = []
        for x in range(len(nums) + 1):
            list1 = []
            for y in range(target + 1):
                list1.append(-1)
            memory.append(list1)
        return self.isPossible(0, target, nums, memory)