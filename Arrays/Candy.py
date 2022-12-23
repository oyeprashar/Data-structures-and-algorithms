"""
Why can't we just iterate over the array and compare the neighbors?
	- This will lead to wrong answer as we want correct left and right answer to compute the correct current ans

How to get the correct left and right answer to get the correct current answer?
	- We will first iterate from left to right
	- We will then iterate from right to left
	- Then we will find max of left and right at each index

Why are we finding the max?
	Let's say the left answer at index i was 3 and right ans was 4
	The question says that we need to allocation more candies to student with more rating
	If we put answer as 3 it will be wrong since 4 was required when you compare the rating at the right
	so 4 will be the right answer
"""
class Solution:
    def candy(self, ratings):

        leftAns = [1] * len(ratings)

        for i in range(1, len(ratings)):

            if ratings[i] > ratings[i - 1]:
                leftAns[i] = leftAns[i - 1] + 1

        rightAns = [1] * len(ratings)

        for j in range(len(ratings) - 2, -1, -1):

            if ratings[j] > ratings[j + 1]:
                rightAns[j] = rightAns[j + 1] + 1

        ans = 0

        for x in range(len(ratings)):
            ans += max(leftAns[x], rightAns[x])

        return ans
