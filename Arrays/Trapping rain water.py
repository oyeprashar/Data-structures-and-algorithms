"""
Trapping Rain Water

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.


Approach :

    Iterating the complete array
        - We need to iterate over all the towers and compute how much water can be trapper above them. Which we keep adding
            to res
        - We compute the water level and if the height of current tower is smaller than the water level, water is trapped!

    How do we compute the water level at each index?

        - The very core of the logic is that water is trapped between two towers and their height is limited by the
            height of the smaller of these two
        - So at each index we need to understand what towers are causing the trapped water at the current index
        - Since we want to maximise the amount of trapped water, these two towers should be the best possible (max)
        - To understand the leftmax and rightmax we use the below helper method. The water level is min of these two
"""


class Solution:

    def generate_left_right_max(self, heights):

        left_max = [0] * len(heights)
        left_max[0] = heights[0]
        for i in range(1, len(heights)):
            left_max[i] = max(left_max[i - 1], heights[i])

        right_max = [0] * len(heights)
        right_max[-1] = heights[-1]
        for i in range(len(heights)-2, -1, -1):
            right_max[i] = max(right_max[i + 1], heights[i])

        return left_max, right_max


    def trap(self, height):

        left_max, right_max = self.generate_left_right_max(height)

        # 0th index and the very last index cannot trap water as they are at the boundary and will leak it
        total_trapped_water = 0
        for i in range(1, len(height) - 1):
            water_level = min(left_max[i], right_max[i]) # the min of these two will limit the height of the water

            # water can only be trapped if current tower is smaller than the waterLevel
            if height[i] < water_level:
                total_trapped_water += water_level - height[i]

        return total_trapped_water

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
