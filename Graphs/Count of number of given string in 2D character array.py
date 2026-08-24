class Solution:

    def isWordPresent(self, currRow, currCol, mat, currIndex, word, visited, directions):

        if currRow < 0 or currRow >= len(mat) or currCol < 0 or currCol >= len(mat[0]):
            return 0

        if (currRow, currCol) in visited or mat[currRow][currCol] !=  word[currIndex]:
            return 0

        # Because we want to make sure even the last char matches. Putting it at the top skips checking the last char
        if currIndex == len(word) - 1:
            return 1


        visited.add((currRow, currCol))
        count = 0
        for rowIncrement, colIncrement in directions:
            count +=  self.isWordPresent(currRow + rowIncrement, currCol + colIncrement, mat, currIndex + 1, word, visited, directions)

        visited.remove((currRow, currCol))
        return count

    def countOccurrence(self, mat, word):

        totalCount = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if mat[i][j] == word[0]:
                    totalCount += self.isWordPresent(i, j, mat, 0, word, set(), directions)

        return totalCount


mat = [
    ['S', 'N', 'B', 'S', 'N'],
    ['B', 'A', 'K', 'E', 'A'],
    ['B', 'K', 'B', 'B', 'K'],
    ['S', 'E', 'B', 'S', 'E']
]
word = "SNAKES"

s = Solution()
print(s.countOccurrence(mat, word))