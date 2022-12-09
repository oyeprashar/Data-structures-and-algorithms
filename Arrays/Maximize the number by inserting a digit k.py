"""
Maximize the number N by inserting given digit at any position

Input: N = 6673, K = 6
Output: 66763
Explanation:
All the numbers formed by inserting K at any position in N are {66673, 66763, 66736}. The maximum among all the formed number is 66763.


Approach:
	We just need to traverse from left to right and find the first number smaller than k and insert k before that
"""


def maximizeNumber(str1, k):
	arr = [int(char) for char in str1]
	smallerIndex = None

	for i in range(len(arr)):
		if arr[i] < k:
			smallerIndex = i
			break

	if smallerIndex is None:
		ans = arr.append(k)
	else:
		ans = arr[:smallerIndex]
		ans.append(k)
		ans.extend(arr[smallerIndex:])

	ansStr = ""
	for num in ans:
		ansStr += str(num)

	return ansStr


print(maximizeNumber("6673", 6))
