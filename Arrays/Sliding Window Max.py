# Time Complexity : O(N)
# Space Complexity: O(K)

from collections import deque


class Solution:
	def maxSlidingWindow(self, nums, k):

		currentWindow = deque([])

		for x in range(k):

			while len(currentWindow) > 0 and nums[x] > nums[currentWindow[-1]]:
				currentWindow.pop()

			currentWindow.append(x)

		ans = []

		for i in range(k, len(nums)):

			ans.append(nums[currentWindow[0]])

			# removing the out of window elements
			while len(currentWindow) > 0 and currentWindow[0] < (i - k + 1):
				currentWindow.popleft()

			# removing elements smaller than the current element in the window
			while len(currentWindow) > 0 and nums[i] > nums[currentWindow[-1]]:
				currentWindow.pop()

			currentWindow.append(i)

		ans.append(nums[currentWindow[0]])

		return ans