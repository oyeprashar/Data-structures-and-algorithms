"""
This is weird because once we select a direction, we want the whole string to be in that direction
"""


class Solution:

    def searchWordHelper(self, currRow, currCol, currIndex, word, mat, incrRow, incrCol):

        if currIndex == len(word):
            return True

        if currRow < 0 or currRow >= len(mat) or currCol < 0 or currCol >= len(mat[0]):
            return False

        if word[currIndex] != mat[currRow][currCol]:
            return False

        if self.searchWordHelper(currRow + incrRow, currCol + incrCol, currIndex + 1, word, mat, incrRow, incrCol):
            return True

        return False

    def searchWord(self, mat, word):

        ans = set()
        directions = [
            (-1, 0), (1, 0),
            (0, -1), (0, 1),
            (-1, -1), (-1, 1),
            (1, -1), (1, 1)
        ]

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if mat[i][j] == word[0]:

                    for incrementRow, incrementCol in directions:

                        if self.searchWordHelper(i, j, 0, word, mat, incrementRow, incrementCol):
                            ans.add((i, j))

        return sorted(list(ans))
