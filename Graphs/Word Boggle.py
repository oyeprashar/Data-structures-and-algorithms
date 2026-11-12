"""
We backtrack the visited because some cells which we marked visited during certain path which did not led to the answer
can be used in another path, we cannot simply block them
"""


from collections import defaultdict

class Solution:

    def isWordPresent(self, i, j, currIndex, word, board, directions, visited):

        if (i, j) in visited:
            return

        if currIndex[0] == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False

        if word[currIndex[0]] !=  board[i][j]:
            return False

        currIndex[0] += 1
        visited.add((i, j))

        for moveRow, moveCol in directions:

            newRow = i + moveRow
            newCol = j + moveCol

            if self.isWordPresent(newRow, newCol, currIndex, word, board, directions, visited):
                return True

        currIndex[0] -= 1
        visited.remove((i, j))
        return False



    def wordBoggle(self, board, dictionary):

        firstCharToWordList = defaultdict(list)

        for word in dictionary:
            firstCharToWordList[word[0]].append(word)


        res = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (1, -1), (1, 1), (-1, -1)]

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] in firstCharToWordList:

                    wordList = firstCharToWordList[board[i][j]]

                    for word in wordList:

                        if word in res:
                            continue

                        if self.isWordPresent(i, j, [0], word, board, directions, set( )):
                            res.add(word)

        return list(res)
