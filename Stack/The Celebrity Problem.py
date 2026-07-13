"""
  - if an element of row i and column j is set to 1 it means ith person knows jth person.
  - Celebrity is the person who knows no one but everyone else knows him!

"""
class Solution:
    def celebrity(self, mat):


        # step 1:
        # Find a candidate who can be the celebrity
        stack  = []
        for row in range(len(mat)):
            stack.append(row)

        while len(stack) >= 2:

            top1 = stack.pop()
            top2 = stack.pop()

            # if top1 knows top2 and top2 does not know top1 --> top2 can be a celebrity. They go back to the stack
            if mat[top1][top2] == 1 and mat[top2][top1] == 0:
                stack.append(top2)

            # if top2 knows top1 but top1 does not know top2 --> top1 can be a celebrity, They go back to the stack
            if mat[top2][top1] == 1 and mat[top1][top2] == 0:
                stack.append(top1)

        if len(stack) == 0:
            return -1

        candidate = stack[-1]

        # step 2:
        # Verify everyone knows this candidate
        for row in range(len(mat)):

            if row == candidate:
                continue

            if mat[row][candidate] == 0:
                return -1

        # step 3:
        # Verify this person knows no one
        for col in range(len(mat[0])):

            if col == candidate:
                continue

            if mat[candidate][col] == 1:
                return -1

        # return the candidate if they pass all the test
        return candidate

mat = [[1, 1, 0],
       [0, 1, 0],
       [0, 1, 1]]

s = Solution()
print(s.celebrity(mat))
